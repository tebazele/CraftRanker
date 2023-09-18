# app.py
# Author : Andre Baldo (http://github.com/andrebaldo/)
# The main file for this login service, this will deal with the login process
# and the login authentication, and logout.
from services.jsonClassEncoder import JsonClassEncoder
from services.customSessionInterface import CustomSessionInterface
from services.auth import Auth
from services.videoinsert import VideoData
from models.loginTokenResult import LoginTokenResult
import flask
import os
import flask_login
from flask import request, jsonify, url_for, abort
from flask_sqlalchemy import SQLAlchemy
import json
import stripe


app = flask.Flask(__name__)

workingDirectory = os.getcwd()
configFile = os.path.join(workingDirectory, 'config.json')

with open(configFile, 'r') as jsonConfig:
    config = json.load(jsonConfig)


# Configurations
ALLOWED_CORS_DOMAIN = 'http://localhost:5173'
app.secret_key = 'asd;lj34asd9fa;l;3'
STRIPE_KEY = config['stripe_secret_key']
jsonClassEncoder = JsonClassEncoder()

login_manager = flask_login.LoginManager()
login_manager.init_app(app)
app.session_interface = CustomSessionInterface()
# End of Configurations section

# print(app.secret_key)
# print(STRIPE_KEY)
# print(ALLOWED_CORS_DOMAIN)

authModule = Auth()
videoModule = VideoData()
with app.app_context():
    from services.mail import mail


@login_manager.user_loader
def load_user(user_id):
    return authModule.load_user(user_id)

# This is a dummy route to test things like uwsgi/nginx/etc


@app.route('/sexybeast')
def sexybeast():
    return 'Jeanne'


@app.route('/public-keys')
def public_keys():
    return jsonify({"key": config['stripe_public_key']})


stripe.api_key = config['stripe_secret_key']
endpoint_secret = 'whsec_029d3af66e4cecba3ae446513094861b1ee553929a26bedf404dc14c6d7e85a0'

# FIXME figure out some way to make register route more secure


@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    secret_token = 'h7p3s3ll14gCRr3gP7g39904-dtc000'
    prod_success_url = 'https://craftranker.jeanneallen.us/form-register'
    prod_cancel_url = 'https://craftranker.jeanneallen.us/plans'
    dev_success_url = 'http://localhost:5173/form-register'
    dev_cancel_url = 'http://localhost/plans'
    session = stripe.checkout.Session.create(
        line_items=[
            {
                'price': "price_1NpaPiHCtKGyoq0UKwu614bT",
                'quantity': 1
            }
        ],
        mode='payment',
        success_url=dev_success_url + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=dev_cancel_url
    )
    print("[THIS IS THE SESSION ID]", session.id)

    # with app.app_context():
    #     from services.mail import purchase
    #     purchase()

    # TODO send an email about purchase
    # send back a some sort of token and append it to the url to allow them to register so just anybody can't go to register

    return jsonify({"sessionURL": session.url, "sessionID": session.id})


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.content_length > 1024 * 1024:
        print('REQUEST TOO BIG')
        abort(400)
    event = None

    payload = request.get_data()
    # print(payload)

    try:
        event = json.loads(payload)
    except:
        print('⚠️  Webhook error while parsing basic request.' + str(e))
        return jsonify(success=False)

    if endpoint_secret:
        sig_header = request.headers.get('stripe-signature')
    #    sig_header = request.environ.get('HTTP_STRIPE_SIGNATURE')
        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, endpoint_secret
            )
        except stripe.error.SignatureVerificationError as e:
            print('⚠️  Webhook signature verification failed.' + str(e))
            return jsonify(success=False)

    if event and event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        print(session)
        if session['payment_status'] == "paid":
            email = session['customer_details']['email']
            print('[EMAIL]', email)
            with app.app_context():
                from services.mail import purchase
                purchase(email)
    return jsonify(success=True)

# Only requests that have an Authorization request reader set with a valid login token
# can access the protected routes, like this '/home' one for example

# NOTE this is how to lock down a route with flask_login
# @app.route('/coursecontent', methods=(['GET']))
# @flask_login.login_required
# def home():
#     print("You are logged in")

#     return 'Home protected by @flask_login.login_required'


@app.route('/videos', methods=(['GET']))
@flask_login.login_required
def getVideos():
    vids = videoModule.getVideos()
    vids_as_dicts = [vid.get_as_dict() for vid in vids]
    # json.dumps turns a list of dictionaries into json
    return json.dumps(vids_as_dicts), 200

# Sets the route for this endpoint, this will configure our web server to receive requests at this path.


@app.route('/register', methods=(['POST']))
def register():
    requestPayload = request.get_json()
    username = requestPayload['email']
    password = requestPayload['password']
    fullName = requestPayload['fullName']

    registerResult = authModule.register(username, password, fullName)
    if registerResult.success == True:
        return jsonClassEncoder.encode(registerResult), 200
    else:
        return jsonClassEncoder.encode(registerResult), 500


# this route will login the user and return a Json Web Token, this token
# will be stored into the client aplication and need to be passed over for each new
# request, via Authorizaton header.
@app.route('/token', methods=(['POST']))
def token():

    authToken = request.headers.get('Authorization')
    activeSession = authModule.GetActiveSession(authToken)
    if activeSession is not None:
        loginResult = LoginTokenResult(
            True, 'Login successful', activeSession.jwToken)
        return jsonClassEncoder.encode(loginResult), 200
        # return "This function is working", 200
    else:
        requestPayload = request.get_json()
        username = requestPayload['email']
        password = requestPayload['password']
        loginResult = authModule.getLoginToken(
            username, password, app.config['SECRET_KEY'])

        if loginResult.success == True:
            return jsonClassEncoder.encode(loginResult), 200
            # return "This is working", 200
        else:
            return jsonClassEncoder.encode(loginResult), 401
            # return "This isn't working ", 401


# This will invalidate the user current user session on the server
@app.route('/logout', methods=(['POST']))
def sessionLogout():

    authToken = request.headers.get('Authorization')
    logoutResult = authModule.SessionLogout(authToken, request.url)
    if logoutResult.success == True:
        return jsonClassEncoder.encode(logoutResult), 200
    else:
        return jsonClassEncoder.encode(logoutResult), 401


# This enable CORS, it means that this server will authorize AJAX calls from
# other domains than the current domain where the API is running
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = ALLOWED_CORS_DOMAIN
    if request.method == 'OPTIONS':
        response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
        headers = request.headers.get('Access-Control-Request-Headers')
        if headers:
            response.headers['Access-Control-Allow-Headers'] = headers

    return response


app.after_request(add_cors_headers)


# Checks if the user is auhenticated for protected routes decorated with @flask_login.login_required
@login_manager.request_loader
def load_user_from_request(request):
    # Get the token from the Authorization request header
    authToken = request.headers.get('Authorization')
    if authToken:
        try:
            # Checks if is there a active session for this token and return his user
            user = authModule.GetUserByToken(authToken)
            return user
        except TypeError:
            pass

            # If it can't find an active session returns None,
    # this will cause the request decorated with @flask_login.login_required been denied
    return None

# @app.route('/coursecontent', methods=(['POST']))
# def addVideoData():
#     requestPayload = request.get_json()
#     username = requestPayload['email']
#     password = requestPayload['password']
#     mobilePhone = requestPayload['mobilePhone']

#     registerResult = authModule.register(username, password, mobilePhone)
#     if registerResult.success == True:
#         return jsonClassEncoder.encode(registerResult), 200
#     else:
#         return jsonClassEncoder.encode(registerResult), 500


if __name__ == '__main__':
    app.run()

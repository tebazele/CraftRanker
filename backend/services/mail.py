from flask import current_app, jsonify, request, render_template, redirect
from flask_mail import Mail, Message
from services.auth import Auth


current_app.config['MAIL_USERNAME'] = "jeanne@craftranker.com"
current_app.config['MAIL_PASSWORD'] = "Myname1sn0*"
current_app.config['MAIL_PORT'] = 587
current_app.config['MAIL_SERVER'] = "mail.privateemail.com"
current_app.config['MAIL_USE_TLS'] = True
current_app.config['MAIL_USE_SSL'] = False
# current_app.config['USE_CREDENTIALS'] = True
# current_app.config['VALIDATE_CERTS'] = True
current_app.config['MAIL_DEFAULT_SENDER'] = "Jeanne@craftranker.com"

mail = Mail(current_app)
authModule = Auth()
# current_app.app_context()

# html = """
# <p>To reset your password, click this link:<p>
# <a href="{{ url_for('current_app.)}}>LINK</a>
# """


@current_app.route('/reset', methods=(['POST']))
def reset():

    requestPayload = request.get_json()
    email = requestPayload['email']
    # Go find the person in the database by their email
    our_user = authModule.GetUserByEmail(email)

    # print("This is our user", our_user)

    msg = Message("Reset Your Password for University of Etsy Courses, CraftRanker",
                  recipients=[email],
                  html=render_template('reset_email.html', user=our_user["fullName"], token="2jd9lk"))
    # mail.send(msg)
    return jsonify(status_code=200, content={"message": "email has been sent"})


@current_app.route('/verified/<token>/<user>', methods=(['GET', 'POST']))
def verified(token, user):
    # If this route is hit (when someone clicks on the link in their email), return the jinja template allowing them to reset their password
    # domain = ''
    # if debug:
    #     domain = 'http://127.0.0.1:5173'
    password = request.form.get('password')
    if password:
        authModule.changePassword(password, user)
        # if debug, return hardcoded url
        # return redirect(domain + '/login', code=302)
        return redirect('http://127.0.0.1:5173/login', code=302)
    # else return relative url

    return render_template('reset_verified.html')

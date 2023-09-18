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
    reset_token = authModule.getResetToken(
        our_user["username"], current_app.config['SECRET_KEY'])
    # print("This is our token", reset_token)

    msg = Message("Reset Your Password for University of Etsy Courses, CraftRanker",
                  recipients=[email],
                  html=render_template('reset_email.html', user=our_user["fullName"], token=reset_token))
    mail.send(msg)


@current_app.route('/verified/<token>/<user>', methods=(['GET', 'POST']))
def verified(token, user):
    # If this route is hit (when someone clicks on the link in their email), return the jinja template allowing them to reset their password
    appSecret = current_app.config['SECRET_KEY']
    user = authModule.verify_reset_token(token, appSecret)
    if not user:
        # FIXME redirect to page that says your password reset link has expired go to login
        return redirect('http://127.0.0.1:5173', code=302)
        # print(user)
    # domain = ''
    # if debug:
    #     domain = 'http://127.0.0.1:5173'
    password = request.form.get('password')
    if password:
        str = authModule.changePassword(password, user)
        print(str)
        # if debug, return hardcoded url
        # return redirect(domain + '/login', code=302)
        return redirect('http://127.0.0.1:5173/login', code=302)
    # else return relative url

    return render_template('reset_verified.html')


# @current_app.route('/purchase', methods=(['GET', 'POST']))
def purchase(email):
    # print('[EMAIL]', email)
    msg = Message("Thank you for your purchase of CraftRanker's University of Etsy Masterclasses",
                  recipients=[email],
                  html=render_template('purchase_confirm.html'))
    mail.send(msg)
    return jsonify(status_code=200, content={"message": "email has been sent"})

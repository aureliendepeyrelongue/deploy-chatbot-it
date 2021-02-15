from flask import render_template, request, redirect,url_for
from app import app, service
from .feed_models import feed_db
from flask import session, flash

@app.route("/")
def home():
    authentication_message = None
    if session.get('login_success_origin') == "success":
        authentication_message = {"status": "success"}
        session.pop('login_success_origin')

    elif session.get('login_success_origin') == "error":
        authentication_message = {"status": "error"}
        session.pop('login_success_origin')

    return render_template("pages/common/index.html",authentication_message = authentication_message)

@app.route("/common/register")
def get_registration_page():
    return render_template("pages/common/registration.html")

@app.route('/common/login',methods = ['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    user = service.login(email=email, password=password)

    if user != None:
        session['authenticated'] = True
        session['user_id'] = user.id
        session['user_first_name'] = user.first_name
        session['login_success_origin'] = "success"
        if user.is_admin == True:
            session['is_admin'] = True
    else:
        session['login_success_origin'] = "error"

    return redirect(url_for("home"))


@app.route('/common/logout',methods = ['POST'])
def logout():
    session.pop('authenticated')
    session.pop('user_id')
    session.pop('user_first_name')
    if session.get('is_admin'):
        session.pop('is_admin')

    return redirect(url_for("home"))


@app.route('/common/register',methods = ['POST'])
def register():
   if request.method == 'POST':
      first_name = request.form['first_name']
      last_name = request.form['last_name']
      email = request.form['email']
      password = request.form['password']
      service_form = request.form['service']

      try:
          service.register(first_name,last_name,email,password,service_form)
      except ValueError:
          registration_message = {"status": "error", "content": "The email is already used, please use un different email"}
          return render_template('pages/common/registration.html', registration_message = registration_message)

   return redirect(url_for("home"))
    

@app.route('/feed')
def feed():
    feed_db()
    return redirect(url_for("home"))




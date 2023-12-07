from flask import Blueprint, render_template, flash, redirect, url_for, session, request
from .models import User
from . import db, oauth, GOOGLE_CLIENT_ID, CLIENT_SECRET

auth = Blueprint('auth', __name__)

google = oauth.register(
    'google',
    client_id = GOOGLE_CLIENT_ID,
    client_secret = CLIENT_SECRET,
    server_metadata_url = 'https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid profile email'}
)

@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            # if check_password_hash(user.password, password):
            if user.password == password:
                 flash('Logged in successfully!', category='success')
                 return redirect('userprofile')
            else:
                flash('Incorrect Password', category='error')
        else:
            flash(' Email doesn\'t exist', category='error')
    return render_template("signin.html", boolean=True)

@auth.route('/login_google')
def login_google():
    redirect_uri = url_for('auth.authorize', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

@auth.route('/signup_google')
def sign_up_google():
    redirect_uri = url_for('auth.authorize', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

@auth.route('/authorize')
def authorize():
    google = oauth.google
    token = google.authorize_access_token()
    resp = token['userinfo']

    session.clear()

    print(resp)
    session['name'] = resp['name']
    session['email'] = resp['email']
    session['obool'] = True
    return redirect('userprofile')

@auth.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@auth.route('/userprofile')
def userprofile():
    name = session['name']
    email = session['email']
    oauth = session['obool']
    user = User.query.filter_by(email=email).first()
    if not user:
        newUser = User(email=email, name=name, oauth=oauth)
        db.session.add(newUser)
        db.session.commit()
    return redirect('/feed')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        name = fname + " " + lname

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists', category='error')
        elif len(email) < 4:
            flash('Email must be valid.', category='error')
        elif len(name) < 3:
            flash('First Name must be more than two characters.', category='error')
        elif password1 != password2:
            flash('Your passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            #add user
            newUser = User(email=email, name=name, password=password1, oauth=False)
            db.session.add(newUser)
            db.session.commit()
            session['name'] = name
            session['email'] = email
            flash('Account Created', category='success')

            return redirect('userprofile')

    return render_template("signup.html")
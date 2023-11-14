from flask import Blueprint, render_template, flash, redirect, url_for, session
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

@auth.route('/login')
def login():
    redirect_uri = url_for('auth.authorize', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

@auth.route('/authorize')
def authorize():
    google = oauth.google
    token = google.authorize_access_token()
    resp = token['userinfo']

    print(resp)
    session['name'] = resp['name']
    session['email'] = resp['email']
    return redirect('userprofile')

@auth.route('/logout')
def logout():
    return "<h1>Logout</h1>"

@auth.route('/signup')
def sign_up():
    return render_template("sign_up.html")

@auth.route('/userprofile')
def userprofile():
    name = session['name']
    email = session['email']
    user = User.query.filter_by(email=email).first()
    if not user:
        newUser = User(email=email, name=name)
        db.session.add(newUser)
        db.session.commit()
    return f'Hello {name}, email: {email}!'
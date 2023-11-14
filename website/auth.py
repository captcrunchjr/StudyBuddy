from flask import Blueprint, render_template, flash, redirect, url_for, session
from .models import User
from . import db, oauth, GOOGLE_CLIENT_ID, CLIENT_SECRET

auth = Blueprint('auth', __name__)

google = oauth.register(
    'google',
    client_id = GOOGLE_CLIENT_ID,
    client_secret = CLIENT_SECRET,
    access_token_url = 'https://accounts.google.com/o/oauth2/token',
    access_token_params = None,
    authorize_url = 'https://accounts.google.com/o/oauth2/auth',
    authorize_params = None,
    api_base_url = 'https://www.googleapis.com/oauth2/v1/',
    server_metadata_url = 'https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'profile email'}
)

@auth.route('/login_google')
def login():
    oauth.crete_client('google')
    redirect_uri = url_for('auth.authorize', external=True)
    return google.authorize_redirect(redirect_uri)

@auth.route('/authorize')
def authorize():
    oauth.create_client('google')
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    resp.raise_for_status()
    profile = resp.json()
    print(profile)
    session['name'] = profile['name']
    session['email'] = profile['email']
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
    return f'Hello {name}, email: {email}!'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from authlib.integrations.flask_client import OAuth

oauth = OAuth()
db = SQLAlchemy()
DB_Name = 'campusbuddies'
GOOGLE_CLIENT_ID = '1077847252138-32ork9nfgi101f34ornknksloqd87e2n.apps.googleusercontent.com' 
CLIENT_SECRET = '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'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "teamgriffindor"

    #database connection info
    username = 'root'
    password = 'password'
    hostname = 'localhost'
    port = '3306'
    app.config['SQLALCHEMY_DATABASE_URI'] =\
            f'mysql://{username}:{password}@{hostname}:{port}/{DB_Name}'
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
    db.init_app(app)
    
    #import and register views blueprints
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    #import models and create tables if necessary
    from .models import User, User_Info
    with app.app_context():
        db.create_all()

    oauth.init_app(app)
    
    return app
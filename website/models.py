from . import db
from sqlalchemy.sql import func

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), nullable=True)
    oauth = db.Column(db.Boolean, nullable=False)

class User_Info(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True,)

class Discipline(db.Model):
    disc_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    
class Degree(db.Model):
    deg_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    disc_ID = db.Column(db.Integer, db.ForeignKey('discipline.disc_id'), nullable=False)

class Course(db.Model):
    course_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    degree_id = db.Column(db.Integer, db.ForeignKey('degree.deg_id'), nullable=False)

class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('degree.deg_id'), nullable=False)
    poster = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_time = db.Column(db.DateTime(timezone=True), server_default=func.now())
    update_time = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=False)

class Comment(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'), nullable=False)
    commenter = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comment_time = db.Column(db.DateTime(timezone=True), server_default=func.now())
    update_time = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    content = db.Column(db.String(500), nullable=False)

class FeedPost(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    poster_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_content = db.Column(db.String(500), nullable=False)
    post_time = db.Column(db.DateTime(timezone=True), server_default=func.now())
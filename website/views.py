from flask import Blueprint, render_template, request, session
from .models import *

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/about')
def about():
    return render_template("about.html")

@views.route('/contact')
def contact():
    return render_template("contact.html")

@views.route('/posttrial', methods=['GET', 'POST'])
def posttrial():
    if request.method == 'POST':
        user = User.query.filter_by(email=session['email']).first()
        poster = user.id
        course_id = 1
        title = request.form.get('title')
        content = request.form.get('content')

        newPost = Post(poster=poster, course_id=course_id, title=title, content=content)
        db.session.add(newPost)
        db.session.commit()
    return render_template("posttrial.html")

@views.route('/commenttrial', methods=['GET', 'POST'])
def commenttrial():
    if request.method == 'POST':
        user = User.query.filter_by(email=session['email']).first()
        commenter = user.id
        post_id = 5
        content = request.form.get('content')

        newPost = Comment(commenter=commenter, post_id=post_id, content=content)
        db.session.add(newPost)
        db.session.commit()
    return render_template("commenttrial.html")
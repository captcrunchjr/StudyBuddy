from flask import Blueprint, render_template, request, session, redirect, url_for
from sqlalchemy import *
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


@views.route('/disciplines', methods=['POST', 'GET'])
def disciplines():
    disciplines = db.session.scalars(select(Discipline).order_by(Discipline.disc_id)).all()
    print(disciplines)
    discArray = []
    for discipline in disciplines:
        numDegrees = Degree.query.filter_by(disc_ID = discipline.disc_id).count()
        disc = {'id': discipline.disc_id, 'name': discipline.name, 'numDeg': numDegrees}
        discArray.append(disc)
    
    return render_template('disciplines.html', discArray = discArray)

@views.route('/degrees/<disc_id>')
def degrees(disc_id):
    degrees = db.session.scalars(select(Degree).where(Degree.disc_ID == disc_id)).all()
    degArray = []
    for degree in degrees:
        numCourses = Course.query.filter_by(degree_id = degree.deg_id).count()
        deg = {'id': degree.deg_id, 'name': degree.name, 'numCourses': numCourses}
        degArray.append(deg)
    
    return render_template('degrees.html', degArray = degArray)

@views.route('/courses/<deg_id>')
def courses(deg_id):
    courses = db.session.scalars(select(Course).where(Course.degree_id == deg_id)).all()
    courseArray = []
    for course in courses:
        numPosts = Post.query.filter_by(course_id = course.course_id).count()
        crs = {'id': course.degree_id, 'name': course.name, 'numPosts': numPosts}
        courseArray.append(crs)
    
    return render_template('courses.html', courseArray = courseArray)

@views.route('/posts/<course_id>', methods=['GET', 'POST'])
def posts(course_id):
    session['course_id'] = course_id
    posts = db.session.scalars(select(Post).where(Post.course_id == course_id)).all()
    postArray = []
    user = None
    if session and 'email' in session:
        user = User.query.filter_by(email=session['email']).first()
    

    for post in posts:
        numComments = Comment.query.filter_by(post_id = post.post_id).count()
        cmt = {'id': post.post_id, 'name': post.title, 'numComments': numComments, 'post_time': post.post_time, 'posterid': post.poster}
        print(cmt)
        postArray.append(cmt)

    if request.method == 'POST':
        poster = user.id
        title = request.form.get('title')
        content = request.form.get('content')

        newPost = Post(poster=poster, course_id=course_id, title=title, content=content)
        db.session.add(newPost)
        db.session.commit()
        
        return redirect(url_for('views.post', post_id = newPost.post_id))

    return render_template("posts.html", postArray = postArray, userid = user.id if user else 0)

@views.route('/post/<post_id>', methods=['GET', 'POST'])
def post(post_id):
    session['post_id'] = post_id
    post = Post.query.filter_by(post_id = post_id).first()
    author = User.query.filter_by(id=Post.poster).first()
    print(post)
    comments = db.session.scalars(select(Comment).where(Comment.post_id == post_id)).all()
    users = User.query.all()
    user = None

    for comment in comments:
        for user in users:
            if comment.commenter == user.id:
                comment.real_name = user.name

    if request.method == 'POST':
        user = User.query.filter_by(email=session['email']).first()
        commenter = user.id
        content = request.form.get('content')

        newPost = Comment(commenter=commenter, post_id=post_id, content=content)
        db.session.add(newPost)
        db.session.commit()

        return redirect(url_for('views.post', post_id = post_id))
    
    if session and 'email' in session:
        user = User.query.filter_by(email=session['email']).first()
    else:
        user = None

    return render_template("post.html", post = post, author=author, comments = comments, userid = user.id if user else 0)

@views.route('/deletepost/<post_id>')
def deletepost(post_id):
    cmtstmt = delete(Comment).where(Comment.post_id == post_id)
    db.session.execute(cmtstmt)
    stmt = delete(Post).where(Post.post_id == post_id)
    db.session.execute(stmt)
    db.session.commit()

    return redirect(url_for('views.posts', course_id = session['course_id']))

@views.route('/deletecomment/<comment_id>')
def deletecomment(comment_id):
    cmtstmt = delete(Comment).where(Comment.comment_id == comment_id)
    db.session.execute(cmtstmt)
    db.session.commit()

    return redirect(url_for('views.post', post_id = session['post_id']))

@views.route('/feed', methods=["POST", 'GET'])
def feed():
    user = User.query.filter_by(email=session['email']).first()
    users = User.query.all()
    posts = db.session.scalars(select(FeedPost)).all()

    for post in posts:
        for user in users:
            if post.poster_id == user.id:
                post.real_name = user.name
    
    if request.method=='POST':
        content=request.form.get('feedpost')

        newPost = FeedPost(poster_id = user.id, post_content = content)
        db.session.add(newPost)
        db.session.commit()

    return render_template("feed.html", username = user.name, feedposts = posts )
from flask import Blueprint,request, render_template, flash,redirect,url_for
from werkzeug.security import generate_password_hash,check_password_hash
from models import User
from app import db
from flask_login import login_user, login_required, logout_user
auth = Blueprint('auth',__name__)


@auth.route('/signup', methods=['GET','POST'],endpoint="signup")
def signup_post():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')

        print(email,name,password)
        user = User.query.filter_by(email=email).first()
        if user:
            flash('User already exists. Please use a different email.', 'error')
            return redirect(url_for('auth.signup'))
        
        new_user = User(email=email,name=name,password=generate_password_hash(password=password,method='pbkdf2:sha256'))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('/signup.html')

@auth.route('/login',methods=['GET','POST'],endpoint="login")
def login_post():
    if request.method == "POST":
        email = request.form.get('email')
        password=request.form.get('password')
        print(email)
        user = User.query.filter_by(email=email).first()

        if not user:
            flash('User doesn\'t exist. please sign up', 'error')
            return redirect(url_for('auth.login'))
        
        login_user(user)
        return redirect(url_for('blog.home'))
    return render_template('login.html')

@auth.route("/logout",endpoint='logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
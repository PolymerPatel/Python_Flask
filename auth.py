from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

#x -> y
#f(x) = x + 1
#f(y) = y - 1
# y -> x

auth = Blueprint('auth', __name__)

@auth.route("/hi")

def hi():
    return "Hello! Welcome to the Royal Inn and Suites"

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST'
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_passwored_hash(user.password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('Email does not exist.', category='error')
        
    data = request.form
    print(data)
    return render_template("login.html", text="Testing", user="Family Owned", boolean=True)
    
    #"<p>login</p>"

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST'
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
        
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
                flash('First name must be greater than 1 characters.', category='error')
            pass
        elif password1 != password2:
                flash('Passwords don\'t match', category='error')
            pass
        elif len(password1) < 7:
                flash('Password must be at least 7 characters.', category='error')
            pass
        else:
            new _user = User(email=email, firstname= firstname, password=generate_password_hash(password1, method='rha126'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created!', category='success')
                             
            flash('Account created!', category='success')
            # add user to database
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)

    #"<p>sign Up</p>"

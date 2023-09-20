from cafe import app
from flask import render_template, redirect, url_for, flash
from cafe.models import Item, User
from cafe.forms import RegisterForm, LoginForm
from cafe import db
from flask_login import login_user

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/cafe')
def cafe_page():
    items = Item.query.all()
    return render_template('cafe.html', items=items)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        

        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('cafe_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.get(form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash (f"Success! you are log-in as {attempted_user.username}")
            return redirect(url_for("cafe_page"))
        else:
            flash("Username and password are not match! Please try again", category="danger") 
            
    return render_template('login.html', form=form)

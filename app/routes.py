from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import Uporabniki
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'Neco'}
    posts = [
        {
            'author': {'username': 'Miha'},
            'body': 'Kupil sem si novo kolo!'
        },
        {
            'author': {'username': 'Ana'},
            'body': 'Rada imam metulje!'
        }
    ]
    return render_template('index.html', title='Domov', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Uporabniki.query.filter_by(uporabnisko_ime=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form, current_user=current_user)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Uporabniki(uporabnisko_ime=form.username.data, e_naslov=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registracija je bila uspešna!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Registracija', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/user/<username>')
@login_required
def user(username):
    user = Uporabniki.query.filter_by(uporabnisko_ime=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Post No.1'},
        {'author': user, 'body': 'Post No.1'}
    ]
    return render_template('user.html', user=user, posts=posts)

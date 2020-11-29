from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


@app.route('/')
@app.route('/domov')
def domov():
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
    return render_template('objave.html', title='Domov', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('domov'))
    return render_template('vpis.html', title='Vpis', form=form)
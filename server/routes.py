from server import app
from flask import render_template


@app.route('/')
@app.route('/domov')
def domov():
    user = {'username': 'Neco'}
    posts = [
        {
            'author': {'username' : 'Miha'},
            'body': 'Kupil sem si novo kolo!'
        },
        {
            'author': {'username': 'Ana'},
            'body': 'Rada imam metulje!'
        }
    ]
    return render_template('domov.html', title='Domov', user=user, posts=posts)

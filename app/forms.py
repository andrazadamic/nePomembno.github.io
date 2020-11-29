from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Uporabniško ime', validators=[DataRequired()])
    password = PasswordField('Geslo', validators=[DataRequired()])
    remember_me = BooleanField('Zapomni si me')
    submit = SubmitField('Vpis')

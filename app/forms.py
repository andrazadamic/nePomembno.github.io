from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import Uporabniki

class LoginForm(FlaskForm):
    username = StringField('Uporabniško ime', validators=[DataRequired()])
    password = PasswordField('Geslo', validators=[DataRequired()])
    remember_me = BooleanField('Zapomni si me')
    submit = SubmitField('login')

class RegistrationForm(FlaskForm):
    username = StringField('Uporabniško ime', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Geslo', validators=[DataRequired()])
    password2 = PasswordField(
        'Ponovi geslo', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registracija')

    def validate_username(self, username):
        user = Uporabniki.query.filter_by(uporabnisko_ime=username.data).first()
        if user is not None:
            raise ValidationError('Prosimo uporabite drugo uporabniško ime.')


    def validate_email(self, email):
        user = Uporabniki.query.filter_by(e_naslov=email.data).first()
        if user is not None:
            raise ValidationError('Prosimo uporabite drugačen elektronski naslov.')

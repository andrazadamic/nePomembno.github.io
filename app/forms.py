from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import Uporabniki, kategorije_query, kategorije_query2


class LoginForm(FlaskForm):
    username = StringField('Uporabniško ime', validators=[DataRequired()])
    password = PasswordField('Geslo', validators=[DataRequired()])
    submit = SubmitField('PRIJAVA')


class RegistrationForm(FlaskForm):
    username = StringField('Uporabniško ime', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Geslo', validators=[DataRequired()])
    password2 = PasswordField(
        'Ponovi geslo', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('REGISTRACIJA')

    def validate_username(self, username):
        user = Uporabniki.query.filter_by(uporabnisko_ime=username.data).first()
        if user is not None:
            raise ValidationError('Prosimo uporabite drugo uporabniško ime.')

    def validate_email(self, email):
        user = Uporabniki.query.filter_by(e_naslov=email.data).first()
        if user is not None:
            raise ValidationError('Prosimo uporabite drugačen elektronski naslov.')


class InputKategorijaForm(FlaskForm):
    ime = StringField('Naslov kategorije', validators=[DataRequired()])
    submit = SubmitField('Vnesi')


class InputVrednostForm(FlaskForm):
    naziv = StringField('Naslov vrednosti', validators=[DataRequired()])
    vrednost = StringField('Vrednost', validators=[DataRequired()])
    kategorija = QuerySelectField('Kategorija', query_factory=kategorije_query,
                                  allow_blank=True, get_label='ime_kategorije')
    submit = SubmitField('Vnesi')

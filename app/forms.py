from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import Users, categories_query


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('LOGIN')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('REGISTRATION')

    def validate_username(self, username):
        user = Users.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please enter different username.')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please enter different email address.')


class InputValueForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    value = StringField('Value', validators=[DataRequired()])
    category = QuerySelectField('Category', query_factory=categories_query,
                                  allow_blank=True, get_label='category_name')
    submit = SubmitField('Submit')

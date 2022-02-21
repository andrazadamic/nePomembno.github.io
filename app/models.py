from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user
from hashlib import md5


#* Working with users
class Users(UserMixin, db.Model):
    # Atributes in the table Users
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), index=True, nullable=False)
    email = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(128))
    categories = db.relationship('Categories', backref='user')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    # Hash and save password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Check if password is correct
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Get the gravatar of the user
    #! Not used yet, maybe implement
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

#* Load user data
@login.user_loader
def load_user(user_id):
    return Users.query.get(user_id)

#* Working with categories
class Categories(db.Model):
    # Atributes in table Categories
    category_id = db.Column(db.INTEGER, primary_key=True, autoincrement=True, nullable=False)
    category_name = db.Column(db.String(50), index=True)
    user_id = db.Column(db.INTEGER, db.ForeignKey('users.id'))
    values = db.relationship('Values', backref='category')

    def __repr__(self):
        return '<{}. {}>'.format(self.category_id, self.category_name)

    def __init__(self, category_name, user_id):
        self.category_name = category_name
        self.user_id = user_id


#* Get all categories of selected user
def categories_query():
    user = Users.query.filter_by(username=current_user.username).first()
    return Categories.query.filter_by(user_id=user.id)

#* Working with notes
class Values(db.Model):
    # Atributes in table Values
    value_id = db.Column(db.INTEGER, primary_key=True, autoincrement=True, nullable=False)
    title = db.Column(db.String(50), index=True)
    value = db.Column(db.String(50), index=True)
    popular = db.Column(db.Boolean, index=True)
    category_id = db.Column(db.INTEGER, db.ForeignKey('categories.category_id'))

    def __repr__(self):
        return '<{}: {} - {}>'.format(self.category_id, self.title, self.value)

    def __init__(self, title, value, category_id):
        self.title = title
        self.value = value
        self.popular = False
        self.category_id = category_id

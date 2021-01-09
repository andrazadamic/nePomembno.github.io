from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5

class Uporabniki(UserMixin, db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    uporabnisko_ime = db.Column(db.String(50), index=True, nullable=False)
    e_naslov = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(128))
    kategorije = db.relationship('Kategorije', backref='uporabnik')

    def __repr__(self):
        return '<User {}>'.format(self.uporabnisko_ime)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.e_naslov.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)


@login.user_loader
def load_user(user_id):
    return Uporabniki.query.get(user_id)


class Kategorije(db.Model):
    id_kategorije = db.Column(db.INTEGER, primary_key=True, autoincrement=True, nullable=False)
    ime_kategorije = db.Column(db.String(50), index=True, nullable=False)
    id_uporabnika = db.Column(db.INTEGER, db.ForeignKey('uporabniki.id'))
    vrednosti = db.relationship('Vrednosti', backref='kategorija')

    def __repr__(self):
        return '<Kategorija {}>'.format(self.ime_kategorije)


class Vrednosti(db.Model):
    id_vrednosti = db.Column(db.INTEGER, primary_key=True, autoincrement=True, nullable=False)
    naziv = db.Column(db.String(50), index=True, nullable=False)
    vrednost = db.Column(db.String(50), index=True, nullable=False)
    id_kategorije = db.Column(db.INTEGER, db.ForeignKey('kategorije.id_kategorije'))

    def __repr__(self):
        return '<Naziv: {} - {}>'.format(self.naziv, self.vrednost)

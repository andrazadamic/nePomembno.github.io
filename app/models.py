from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user
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
    ime_kategorije = db.Column(db.String(50), index=True)
    id_uporabnika = db.Column(db.INTEGER, db.ForeignKey('uporabniki.id'))
    vrednosti = db.relationship('Vrednosti', backref='kategorija')

    def __repr__(self):
        return '<{}. {}>'.format(self.id_kategorije, self.ime_kategorije)

    def __init__(self, ime_kategorije, id_uporabnika):
        self.ime_kategorije = ime_kategorije
        self.id_uporabnika = id_uporabnika


def kategorije_query():
    uporabnik = Uporabniki.query.filter_by(uporabnisko_ime=current_user.uporabnisko_ime).first()
    return Kategorije.query.filter_by(id_uporabnika=uporabnik.id)


def kategorije_query2(form_data):
    kategorija = Kategorije.query.filter_by(ime_kategorije=form_data).first()
    return kategorija.id_kategorije


class Vrednosti(db.Model):
    id_vrednosti = db.Column(db.INTEGER, primary_key=True, autoincrement=True, nullable=False)
    naziv = db.Column(db.String(50), index=True)
    vrednost = db.Column(db.String(50), index=True)
    priljubljeno = db.Column(db.Boolean, index=True)
    id_kategorije = db.Column(db.INTEGER, db.ForeignKey('kategorije.id_kategorije'))

    def __repr__(self):
        return '<{}: {} - {}>'.format(self.id_kategorije, self.naziv, self.vrednost)

    def __init__(self, naziv, vrednost, id_kategorije):
        self.naziv = naziv
        self.vrednost = vrednost
        self.priljubljeno = False
        self.id_kategorije = id_kategorije

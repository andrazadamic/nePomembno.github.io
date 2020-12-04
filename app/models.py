from app import db


class Uporabniki(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True, nullable=False)
    uporabnisko_ime = db.Column(db.String(50), index=True, unique=True, nullable=False)
    e_naslov = db.Column(db.String(100), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.uporabnisko_ime)
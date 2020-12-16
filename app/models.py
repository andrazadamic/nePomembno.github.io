from app import db


class Uporabniki(db.Model):
    id_uporabnika = db.Column(db.INTEGER, primary_key=True, autoincrement=True, nullable=False)
    uporabnisko_ime = db.Column(db.String(50), index=True, unique=True, nullable=False)
    e_naslov = db.Column(db.String(100), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    kategorije = db.relationship('Kategorije', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.uporabnisko_ime)


class Kategorije(db.Model):
    id_kategorije = db.Column(db.INTEGER, primary_key=True, autoincrement=True, nullable=False)
    ime_kategorije = db.Column(db.String(50), index=True, nullable=False)
    id_uporabnika = db.Column(db.INTEGER, db.ForeignKey('id_uporabnika'))

    def __repr__(self):
        return '<Kategorija {}>'.format(self.ime_kategorije)


class Vrednosti(db.Model):
    id_vrednosti = db.Column(db.INTEGER, primary_key=True, autoincrement=True, nullable=False)
    naziv = db.Column(db.String(50), index=True, nullable=False)
    vrednost = db.Column(db.String(50), index=True, nullable=False)
    id_kategorije = db.Column(db.String(50), db.ForeignKey('id_kategorije'))

    def __repr__(self):
        return '<Naziv: {} - {}>'.format(self.naziv, self.vrednost)

# ---MIGRATE NI BIL IZVEDEN--- #

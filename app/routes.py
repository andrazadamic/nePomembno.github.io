from app import app, db
from flask import render_template, flash, redirect, url_for, request, jsonify
from app.forms import LoginForm, RegistrationForm, InputVrednostForm, InputKategorijaForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import Uporabniki, Vrednosti, Kategorije
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index(*args):
    uporabnik = Uporabniki.query.filter_by(uporabnisko_ime=current_user.uporabnisko_ime).first()
    kategorije_all = Kategorije.query.filter_by(id_uporabnika=uporabnik.id).all()
    kategorije_id = []
    vrednosti = []
    kategorije_count = []
    id = 'index'

    for kategorija in kategorije_all:
        kategorije_id.append(kategorija.id_kategorije)
        kategorije_count.append(Vrednosti.query.filter_by(id_kategorije=kategorija.id_kategorije).count())
    for vrednost in kategorije_id:
        if id == 'index':
            temp_vrednost = Vrednosti.query.filter_by(id_kategorije=vrednost).all()
        else:
            temp_vrednost = Vrednosti.query.all()
        if temp_vrednost:
            vrednosti = vrednosti + list(temp_vrednost)
            vrednosti_count = len(vrednosti)

    form = InputKategorijaForm()
    if form.validate_on_submit():
        kategorija = Kategorije(ime_kategorije=form.ime.data, id_uporabnika=uporabnik.id)
        if Kategorije.query.filter_by(ime_kategorije=form.ime.data, id_uporabnika=uporabnik.id).first() is not None:
            flash('Kategorija s tem imenom že obstaja! Izberite drugo ime!')
            return redirect(url_for('index'))
        db.session.add(kategorija)
        db.session.commit()
        flash('Uspešno ste dodali novo kategorijo!')
        return redirect(url_for('index'))

    form2 = InputVrednostForm()
    if form2.validate_on_submit():
        nova_vrednost = Vrednosti(naziv=form2.naziv.data, vrednost=form2.vrednost.data,
                                  id_kategorije=form2.kategorija.data.id_kategorije)
        # if Vrednosti.query.filter_by(naziv=form2.naziv.data,
        # id_kategorije=kategorija_izbira.id_kategorije).first() is not None:
        # flash('Vrednost že obstaja! Uredite obstoječo ali ustvarite novo vrednost!')
        #  return redirect(url_for('index'))
        db.session.add(nova_vrednost)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html', title='Domov', form=form, form2=form2, kategorije=kategorije_all,
                           vrednosti=vrednosti, kategorije_count=kategorije_count, kategorije_len=len(kategorije_count),
                           vrednosti_count=vrednosti_count)


def filter_kategorija(id):
    vrednosti = Vrednosti.query.filter_by(id_kategorije=kategorija.id_kategorije).all()
    return vrednosti


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form2 = LoginForm()
    if form2.validate_on_submit():
        user = Uporabniki.query.filter_by(uporabnisko_ime=form2.username.data).first()
        if user is None or not user.check_password(form2.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form2, current_user=current_user)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Uporabniki(uporabnisko_ime=form.username.data, e_naslov=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registracija je bila uspešna!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Registracija', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/kategorija/<int:id>')
@login_required
def kategorija(id):


    uporabnik = Uporabniki.query.filter_by(uporabnisko_ime=current_user.uporabnisko_ime).first()
    kategorije_all = Kategorije.query.filter_by(id_uporabnika=uporabnik.id).all()
    kategorije_id = []
    vrednosti = Vrednosti.query.filter_by(id_kategorije=id).all()
    kategorije_count = []
    vrednosti_count = 0

    for kategorija in kategorije_all:
        kategorije_id.append(kategorija.id_kategorije)
        kategorije_count.append(Vrednosti.query.filter_by(id_kategorije=kategorija.id_kategorije).count())
    for id in kategorije_id:
        vrednosti_count += Vrednosti.query.filter_by(id_kategorije=id).count()


    form = InputKategorijaForm()
    if form.validate_on_submit():
        kategorija = Kategorije(ime_kategorije=form.ime.data, id_uporabnika=uporabnik.id)
        if Kategorije.query.filter_by(ime_kategorije=form.ime.data, id_uporabnika=uporabnik.id).first() is not None:
            flash('Kategorija s tem imenom že obstaja! Izberite drugo ime!')
            return redirect(url_for('index'))
        db.session.add(kategorija)
        db.session.commit()
        flash('Uspešno ste dodali novo kategorijo!')
        return redirect(url_for('index'))

    form2 = InputVrednostForm()
    if form2.validate_on_submit():
        nova_vrednost = Vrednosti(naziv=form2.naziv.data, vrednost=form2.vrednost.data,
                                  id_kategorije=form2.kategorija.data.id_kategorije)
        # if Vrednosti.query.filter_by(naziv=form2.naziv.data,
        # id_kategorije=kategorija_izbira.id_kategorije).first() is not None:
        # flash('Vrednost že obstaja! Uredite obstoječo ali ustvarite novo vrednost!')
        #  return redirect(url_for('index'))
        db.session.add(nova_vrednost)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html', title='Domov', form=form, form2=form2, kategorije=kategorije_all,
                           vrednosti=vrednosti, kategorije_count=kategorije_count, kategorije_len=len(kategorije_count),
                           vrednosti_count=vrednosti_count)
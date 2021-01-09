from app import app, db
from app.models import Uporabniki, Kategorije


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Uporabniki': Uporabniki, 'Kategorije': Kategorije}

app.debug = True

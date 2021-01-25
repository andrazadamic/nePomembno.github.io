from itsdangerous import URLSafeTimedSerializer
from app import app


def generate_confirmation_token(e_naslov):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(e_naslov, salt=app.config['SECURITY_PASSWORD_SALT'])

def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        e_naslov = serializer.loads(
            token,
            salt=app.config['SECRET_PASSWORD_SALT'],
            max_age=expiration
        )
    except:
        return False
    return e_naslov
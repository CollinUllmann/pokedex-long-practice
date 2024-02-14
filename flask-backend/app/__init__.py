
# import statement for CSRF
from flask_wtf.csrf import CSRFProtect, generate_csrf

import os
from .config import Configuration
from flask import Flask
from .models import db
from flask_migrate import Migrate
from .routes import pokemon_routes

app = Flask(__name__)
app.config.from_object(Configuration)

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(pokemon_routes, url_prefix='/api/pokemon')

# after request code for CSRF token injection
@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response

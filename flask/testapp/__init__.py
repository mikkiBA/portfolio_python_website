from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('testapp.config')
app.secret_key = 'secret'

db = SQLAlchemy(app)
from .models import site_db

import testapp.views

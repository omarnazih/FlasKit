from flask import Flask
from pony.orm import *

import os

persistent_path = os.getenv("PERSISTENT_STORAGE_DIR", os.path.dirname(os.path.realpath(__file__)))

app = Flask(__name__)
db = Database()

from app import views

with app.app_context():
    db.bind(provider='sqlite', filename=os.path.join(persistent_path, 'db.sqlite'), create_db=True)
    db.generate_mapping(create_tables=True)


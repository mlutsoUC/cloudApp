import os
from flask import Flask, g
from config import Config
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)

from app import routes

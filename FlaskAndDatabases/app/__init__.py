from os import path

from flask import Flask

STATIC_DIR = 'STATIC_DIR'

template_dir = path.join(path.dirname(path.dirname(__file__)), 'templates')

app = Flask(__name__, template_folder=template_dir)
app.config[STATIC_DIR] = path.join(path.dirname(path.dirname(__file__)), 'static')

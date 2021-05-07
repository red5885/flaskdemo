from flask import Flask,url_for
from markupsafe import escape
import dashboard.views

app = Flask(__name__)
app.config.from_pyfile('flaskdemo/config.py')

app.add_url_rule('/dashboard', 'dashboard.views.index', dashboard.views.index)
app.add_url_rule('/', index)

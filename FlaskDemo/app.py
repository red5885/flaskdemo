from flask import Flask,url_for
from markupsafe import escape
import dashboard, main
from flaskdemo import urls

app = Flask(__name__)
app.config.from_pyfile('flaskdemo/config.py')
#urls.init_routes(app)

app.add_url_rule('/dashboard', 'dashboard.views.index', dashboard.views.index)
app.add_url_rule('/', 'main.views.index', main.views.index)
app.add_url_rule('/login', 'main.views.login', main.views.login)
app.add_url_rule('/profile/<username>', 'main.views.profile', main.views.profile)

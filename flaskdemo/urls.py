from flask import Flask

def init_routes(app):
    app.add_url_rule('/dashboard', 'dashboard.views.index', dashboard.views.index)
    app.add_url_rule('/', main.views.index)
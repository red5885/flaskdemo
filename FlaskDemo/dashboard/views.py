from flask import Flask

def initViews(app):
    app.add_url_rule('/dashboard', view_func = index)
    
def index(request = None):
    return 'This is the dash index'
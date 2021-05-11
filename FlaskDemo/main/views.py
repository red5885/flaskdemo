from markupsafe import escape

def index():
    return 'index'

def login():
    return 'login'

def profile(username):
    return '{}\'s profile'.format(escape(username))
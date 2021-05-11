def initViews(app):
    app.add_url_rule('/dashboard', view_func = index)
    
def index():
    return 'This is the dash index'
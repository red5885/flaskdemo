app.add_url_rule('/dashboard', 'dashboard.views.index', dashboard.views.index)
app.add_url_rule('/', index)
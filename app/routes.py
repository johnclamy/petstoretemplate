from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Jonathan'}
    return '''
    <html>
    <head>
        <title>Microblog | Home page</title>
    </head>
    <body>
        <h1>Hello, {}!</h1>
    </body>
    </html>
'''.format(user['username'])

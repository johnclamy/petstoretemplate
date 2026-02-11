from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = { 'username': 'Jonathan'}
    posts = [
        {
            'author': {'username': 'Molly'},
            'body': 'React.js and Flask are so cool together!'
        },
        {
            'author': {'username': 'Amir'},
            'body': 'I love Python and JavaScript!'
        }
    ]

    return render_template('index.html', title='Home Page', user=user, posts=posts)

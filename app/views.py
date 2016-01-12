from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'nickname': 'Manuel'} # place holder for now
    posts = [ # fake array of posts
        {
            'author': {'nickname': 'Joe'},
            'body': 'I sure want to go skiing today!'
        },
        {
            'author': {'nickname': 'Amy'},
            'body': 'Hello, world!'
        }

    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

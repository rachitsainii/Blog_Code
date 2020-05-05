from flask import Flask, render_template , url_for

posts = [
    {
        'author': 'Rachit Saini',
        'title': 'Blog Post 1',
        'content': "First Post Content",
        'date': 'May 2020'
    },
    {
        'author': 'Naman Saini',
        'title': 'Blog Post 2',
        'content': "Second Post Content",
        'date': 'April 2020'
    },
    {
        'author': 'Random Person',
        'title': 'Blog Post n',
        'content': "nth Post Content",
        'date': 'month year '
    }

]

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html',posts = posts)


@app.route('/about')
def about():
    return render_template('about.html', title = 'About')


app.run(debug=True)

from flask import Flask, render_template, url_for , flash , redirect
from Forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f8d35b418f70c0ab25119ec5313f05c7'

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


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!" , "success")
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET' , 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash("You have been logged in !" , 'success')
            return redirect(url_for('home'))
        else:
            flash("Login Unsuccessful ! Please check Username or Password." , 'danger')

    return render_template('login.html', title='Login', form=form)


app.run(debug=True)

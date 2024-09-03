from flask import Flask, jsonify, request
from markupsafe import escape
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


@app.route("/<name>")
def hello(name):
    return f"Hello {escape(name)}"


@app.route('/about')
def about_me():
    return '<h1> This is Daniel</h1>'


@app.route('/posts')
def show_posts():
    return '<h1>This is my post page</h1>'


@app.route('/projects')
def show_projects():
    return '<h1>This is my Project page</h1>'


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="POST">
    <p><input name="username" type="text" /></p>
    <p><input name="password" type="password"/></p>
    <p><button type="submit">Sign IN</button></p>
    </form>'''

    # return '''<form action="/signin" method="POST">
    #           <p><input name="username"></p>
    #           <p><input name="password" type="password"></p>
    #           <p><button type="submit">Sign In</button></p>
    #           </form>'''


@app.route('/signin', methods=['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h1>Welcome, home!</h1>'
    return '<h1>Wrong username or password.</h1>'


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=8080)

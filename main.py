from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import render_template
from static.scripts import info

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html", error=error)


@app.route('/')
def index():
    response = make_response(redirect('/index'))

    return response


@app.route('/index')
def hello():

    return render_template('index.html', tab_title="Welcom! |")


@app.route('/about-me')
def about_me():
    projects = info.projects
    hobbies = info.hobbies

    return render_template('about-me.html', projects=projects, hobbies=hobbies, tab_title="About me |")


@app.route('/certifications')
def certifications():
    cert = info.cert

    return render_template('certifications.html', cert=cert, tab_title="Certifications |")


@app.route('/timeline')
def timeline():

    return render_template('timeline.html', tab_title="Timeline |")

if __name__ == "__main__":
    app.run()
from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import render_template


app = Flask(__name__)


@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/index'))
    response.set_cookie('user_ip', user_ip)

    return response


@app.route('/index')
def hello():
    user_ip = request.cookies.get('user_ip')

    return render_template('index.html', user_ip=user_ip)


@app.route('/about-me')
def about_me():
    
    return render_template('about-me.html')



@app.route('/certifications')
def certifications():
    
    return render_template('certifications.html')


@app.route('/timeline')
def timeline():
    
    return render_template('timeline.html')



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
    projects = {
        "This Web Site": "This web site was developed using HTML, CSS and JavaScript.",
        "Vision": "Developing a low cost vision system for detection of missing components on UUT through python.",
        "Software Migration": "Migration of our testing software from LabVIEW to python, this includes a wide testing platforms. We selected Django due to it is open source.",
        "Vibration Analisis": "An application based on LabVIEW for vibration analysis for rotating machinery.",
        "Thesis": "'Lead Acid Battery Backup Time Estimation Using LabVIEW for Traction Systems in Electric Vehicles'. This model was capable to estimate State of Charge, Backup Time and Autonomy of the vehicle. It also included the mathematical modeling of a vehicle.",
        "Monophase Inverter": "Design and implementation of a monophase inverter using LabVIEW as control interface.",
        "Power DC-DC Converter": "Design and implementation of a power electronics system for electrical Vehicles using LabVIEW as control interface.",
        "Git Repository Handler": "Developed a shell script capable to handle conflict issues on local repositories in order to complete the update request.",
        "Software Auto Installer": "An application capable to install a varios packages of several softwares in order to automate a repetitive task through shell scripting.",
        "Assembly": "Various scripts with the capability of: control temperature, control three-pashe inverters, serial communication and digital multiplex systems.",
    }

    hobbies = [{
        "hobbi": {
            "title": "Athleticism",
            "img": "static/img/2th.jpg",
            "compress": "static/img/2th.jpg",
        }, },
        {
        "hobbi": {
            "title": "Drawing",
            "img": "static/img/drawing_1.png",
            "compress": "static/img/compress/drawing_1.png",
        }, },
        {
        "hobbi": {
            "title": "Drawing",
            "img": "static/img/drawing_2.png",
            "compress": "static/img/compress/drawing_2.png",
        }, },
    ]
    return render_template('about-me.html', projects=projects, hobbies=hobbies)


@app.route('/certifications')
def certifications():
    cert = [
        {
            "cert": {
                "title": "Basic Python Course",
                "img": "static/img/certifications/basic_python.png",
                "compress": "static/img/compress/certifications/basic_python.png",
                "alt": "Basic Python Course Certification",
                "link":"https://platzi.com/p/Conseicka/",
            }
        }, {
            "cert": {
                "title": "Intermediate Python Course",
                "img": "static/img/certifications/inter_python.png",
                "compress": "static/img/compress/certifications/inter_python.png",
                "alt": "Intermediate Python Course Certification",
                "link":"https://platzi.com/p/Conseicka/",
            }
        }, {
            "cert": {
                "title": "Professional Python Course",
                "img": "static/img/certifications/prof_python.png",
                "compress": "static/img/compress/certifications/prof_python.png",
                "alt": "Professional Python Course Certification",
                "link":"https://platzi.com/p/Conseicka/",
            },
        },{
            "cert": {
                "title": "CSS Course",
                "img": "static/img/certifications/css.png",
                "compress": "static/img/compress/certifications/css.png",
                "alt": "CSS Course Certification",
                "link":"https://platzi.com/p/Conseicka/",
            },
        },{
            "cert": {
                "title": "Data Science Bussiness",
                "img": "static/img/certifications/data.png",
                "compress": "static/img/compress/certifications/data.png",
                "alt": "Data Science Bussiness Certification",
                "link":"https://platzi.com/p/Conseicka/",
            },
        },{
            "cert": {
                "title": "DevOps Course",
                "img": "static/img/certifications/devops.png",
                "compress": "static/img/compress/certifications/devops.png",
                "alt": "DevOps Course Certification",
                "link":"https://platzi.com/p/Conseicka/",
            },
        },{
            "cert": {
                "title": "Git and GitHub Course",
                "img": "static/img/certifications/git.png",
                "compress": "static/img/compress/certifications/git.png",
                "alt": "Git and GitHub Course Certification",
                "link":"https://platzi.com/p/Conseicka/",
            },
        },{
            "cert": {
                "title": "Computational Thinking with Python",
                "img": "static/img/certifications/pensamiento_python.png",
                "compress": "static/img/compress/certifications/pensamiento_python.png",
                "alt": "Computational Thinking with Python Certification",
                "link":"https://platzi.com/p/Conseicka/",
            },
        },{
            "cert": {
                "title": "Oriented Object Programming",
                "img": "static/img/certifications/poo.png",
                "compress": "static/img/compress/certifications/poo.png",
                "alt": "Oriented Object Programming Certification",
                "link":"https://platzi.com/p/Conseicka/",
            },
        },{
            "cert": {
                "title": "POO with Python",
                "img": "static/img/certifications/poo_python.png",
                "compress": "static/img/compress/certifications/poo_python.png",
                "alt": "POO with Python Certification",
                "link":"https://platzi.com/p/Conseicka/",
            },
        },{
            "cert": {
                "title": "Basic Shell Programming",
                "img": "static/img/certifications/shell.png",
                "compress": "static/img/compress/certifications/shell.png",
                "alt": "Basic Shell Programming Certification",
                "link":"https://platzi.com/p/Conseicka/",
            },
        },{
            "cert": {
                "title": "Command Line Basics",
                "img": "static/img/certifications/terminal.png",
                "compress": "static/img/compress/certifications/terminal.png",
                "alt": "Command Line Basics Certification",
                "link":"https://platzi.com/p/Conseicka/",
            },
        },{
            "cert": {
                "title": "Customer Service vs Customer Experience",
                "img": "static/img/certifications/svx.png",
                "compress": "static/img/compress/certifications/svx.png",
                "alt": "Customer Service vs Customer Experience Certification",
                "link":"https://www.linkedin.com/in/yami-almaguer-gil/",
            },
        },{
            "cert": {
                "title": "Managing Project Based Work",
                "img": "static/img/certifications/gtxp.png",
                "compress": "static/img/compress/certifications/gtxp.png",
                "alt": "Managing Project Based Work Certification",
            },
        },{
            "cert": {
                "title": "LabVIEW CLAD",
                "img": "static/img/certifications/labview.png",
                "compress": "static/img/compress/certifications/labview.png",
                "alt": "LabVIEW CLAD Certification",
                "link":"",
            },
        },
    ]
    return render_template('certifications.html', cert=cert)


@app.route('/timeline')
def timeline():

    return render_template('timeline.html')

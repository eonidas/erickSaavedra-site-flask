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
            "hobbi":{
            "title": "Athleticism",
            "img": "static/img/2th.jpg",
            "compress": "static/img/2th.jpg",
        },}, 
            { 
            "hobbi":{
            "title": "Drawing",
            "img": "static/img/drawing_1.png",
            "compress": "static/img/compress/drawing_1.png",
        },}, 
            { 
            "hobbi":{
            "title": "Drawing",
            "img": "static/img/drawing_2.png",
            "compress": "static/img/compress/drawing_2.png",
        },},
    ]
    return render_template('about-me.html', projects=projects, hobbies=hobbies)



@app.route('/certifications')
def certifications():
    
    return render_template('certifications.html')


@app.route('/timeline')
def timeline():
    
    return render_template('timeline.html')



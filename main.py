from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:passwword@localhost/db_name'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/draic_web'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Contact(db.Model):
    ''' 
    sr_num , name, email, contact, message, date
    '''

    sr_num = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(50),  nullable=False)
    contact = db.Column(db.String(12),  nullable=False)
    message = db.Column(db.String(120),  nullable=True)
    check = db.Column(db.String(120),  nullable=True)
    date = db.Column(db.String(20),  nullable=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/achievements")
def achievements():
    return render_template("achievements.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/contactus", methods =['GET', 'POST'])
def contactus():
    if(request.method == 'POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        contact = request.form.get('contact')
        msg = request.form.get('msg')
        check = request.form.get('check')
        entry = Contact(name=name, email=email, contact=contact, message = msg, check=check, date = datetime.now())
        db.session.add(entry)
        db.session.commit()
    return render_template("contactus.html")

app.run(debug= True)

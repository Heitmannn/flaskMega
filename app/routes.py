from flask import render_template 
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'name':'Sivert', 'age':322}
    intzz = ["Matte", "progammering", "trening"]
    return render_template("index.html", title="home!", intzz=intzz, user=user)

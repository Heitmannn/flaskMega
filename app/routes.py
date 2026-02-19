from flask import render_template, flash, redirect, session, url_for
from app import app
from app.forms import Loginform 

@app.route('/')
@app.route('/index')
def index():
    user = {'name':session.get("username", "guest"), 'age':322}
    intzz = ["Matte", "progammering", "trening"]
    return render_template("index.html", title="home!", intzz=intzz, user=user)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = Loginform()
    if form.validate_on_submit():
        flash(f"Jeg vet hvem du er {form.username.data}") 
        session["username"] = form.username.data
        return redirect(url_for("index"))
    else:
         print(f"Failed loggin for {form.username.data}")
    return render_template("login.html", title="Log in", form=form)



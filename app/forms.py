from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, BooleanField, PasswordField
from wtforms.validators import InputRequired


class Loginform(FlaskForm):
    username = StringField('Brukernavn', validators=[InputRequired()])
    password = PasswordField("Passord", validators=[InputRequired()])
    remember_me = BooleanField('Husk meg')
    submit   = SubmitField('logg inn')


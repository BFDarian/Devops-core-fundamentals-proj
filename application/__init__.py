from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField
import os


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dataTeam.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "secret_key"

db = SQLAlchemy(app)

from application import forms
from application import routes
from application import models  
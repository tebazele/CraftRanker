# databaseCreation.py
# Author : Andre Baldo (http://github.com/andrebaldo/)
# Make sure that you have a SQL Server running in your local host, check also the instance
# name, in some installations the server path will be 'localhost/SQLEXPRESS' in this case,
# update the SERVER variable below accordingly
# This script creates the tables User and UserSession, just execute:$python databaseCreation.py
# from your command promt, tested just on Windows.
import flask_login
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
import os
# from videodata import videos


app = Flask(__name__)

workingDirectory = os.getcwd()
configFile = os.path.join(workingDirectory, 'config.json')

with open(configFile, 'r') as jsonConfig:
    config = json.load(jsonConfig)

DATABASE_CONNECTION = config['database_connection_string']
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION

db = SQLAlchemy(app)

app.app_context().push()


class User(db.Model, flask_login.mixins.UserMixin):
    __tablename__ = 'User'

    # Name of the table in our database
    # Defining the columns
    userId = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    mobilePhone = db.Column(db.String(80), unique=False, nullable=True)

    def get_id(self):
        return str(self.userId)


class UserSession(db.Model):
    __tablename__ = 'UserSession'  # Name of the table in our database
    # Defining the columns
    userSessionId = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, nullable=False)
    loginDate = db.Column(db.DateTime, nullable=False)
    expireDate = db.Column(db.DateTime, nullable=False)
    loggedOut = db.Column(db.Boolean, nullable=False)
    jwToken = db.Column(db.String(4000), nullable=False)
    url = db.Column(db.String(4000), nullable=True)
    logoutDate = db.Column(db.DateTime, nullable=True)


class Videos(db.Model):
    __tablename__ = 'Videos'
    __table_args__ = {'sqlite_autoincrement': True}

    videoId = db.Column(db.Integer, primary_key=True)
    sqlite_autoincrement = True
    youtubeId = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    series = db.Column(db.String(255), nullable=False)
    module = db.Column(db.Integer, nullable=False)


db.create_all()
db.session.commit()

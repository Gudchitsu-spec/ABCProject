from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from extencions import db
from models.interval import Interval
from models.group import Group
from models.Schedule import Schedule
from models.Lecturer import Lecturer
from models.Subject import Subject

from Routes.Lecturers import lecturers
from Routes.Intervals import intervals
app = Flask(__name__)

app.config["Debug"]= True
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.register_blueprint(lecturers)
app.register_blueprint(intervals)

if __name__ == '__main__':
    app.run()

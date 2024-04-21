from App.database import db
from .exercise import *

class Routine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'))
    exercise = db.relationship('Exercise')

    def __init__(self, name, user_id, exercise_id):
        self.name = name
        self.user_id = user_id
        self.exercise_id = exercise_id
from App.database import db

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(255), nullable=False)
    muscle = db.Column(db.String(255), nullable=False)
    equipment = db.Column(db.String(255), nullable=False)
    difficulty = db.Column(db.String(255), nullable=False)
    instructions = db.Column(db.String(255), nullable=False) 

    def __init__(self, name, type, muscle, equipment, difficulty, instructions):
        self.name = name,
        self.type = type,
        self.muscle = muscle
        self.equipment = equipment
        self.difficulty = difficulty
        self.instructions = instructions
        
    def get_json(self):
        return {
            'exercise_id': self.id,
            'name': self.name,
            'type': self.type,
            'muscle': self.muscle,
            'equipment': self.equipment,
            'difficulty': self.difficulty,
            'instructions': self.instructions
        }
       

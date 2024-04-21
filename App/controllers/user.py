from App.models import User
from App.database import db

def create_user(username, password):
    newuser = User(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None

def create_routine(self, exercise_id, name):
    exercise = Routine.query.get(exercise_id)
    if exercise:
        try:
            new_exercise = Routine(name, self.id, exercise_id)
            db.session.add(new_exercise)
            db.session.commit()
            return new_exercise
        except Exception as e:
            print(e)
            db.session.rollback()
            return None
    return None

def remove_routine(self, exercise_id):
    exercise = Routine.query.get(exercise_id)
    if exercise.user == self:
        db.session.delete(exercise)
        db.session.commit()
        return True
    return None

def rename_routine(self, exercise_id, name):
    exercise = Routine.query.get(exercise_id)
    if exercise.user == self:
        exercise.name = name
        db.session.add(exercise)
        db.session.commit()
        return True
    return None

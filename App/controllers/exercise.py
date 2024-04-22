import requests, json 
from App.models import Exercise
from App.database import db

def parse_exercises():
    abdominals_exercises = find_exercises('abdominals')
    abductors_exercises = find_exercises('abductors')
    adductors_exercises = find_exercises('adductors')
    biceps_exercises = find_exercises('biceps')
    calves_exercises = find_exercises('calves')
    chest_exercises = find_exercises('chest')
    forearms_exercises = find_exercises('forearms')
    glutes_exercises = find_exercises('glutes')
    hamstrings_exercises = find_exercises('hamstrings')
    lats_exercises = find_exercises('lats')
    lower_back_exercises = find_exercises('lower_back')
    middle_back_exercises = find_exercises('middle_back')
    neck_exercises = find_exercises('neck')
    quadriceps_exercises = find_exercises('quadriceps')
    traps_exercises = find_exercises('traps')
    triceps_exercises = find_exercises('triceps')

def find_exercises(muscle_group):
    api_url = 'https://api.api-ninjas.com/v1/exercises?muscle={}'.format(muscle_group)
    exercises = requests.get(api_url, headers={'X-Api-Key': '34ECD4LQjf7k/KSQABanUg==kRrodx9CuPCV9pAH'}).json()

    for exercise in exercises:
        new_exercise = Exercise(
            name=exercise['name'],
            type=exercise['type'],
            muscle=exercise['muscle'],
            equipment=exercise['equipment'],
            difficulty=exercise['difficulty'],
            instructions=exercise['instructions']
        )

        db.session.add(new_exercise)
    db.session.commit()

def get_all_exercises_by_muscle(muscle):
    return Exercise.query.filter_by(muscle=muscle)

def get_all_exercises():
  return Exercise.query.all()

def get_exercise_by_id(id):
    return Exercise.query.filter_by(id=id).first()

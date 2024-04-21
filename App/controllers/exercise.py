import requests, json 
from App.models import Exercise
from App.database import db

def parse_exercises():
  api_url = 'https://api.api-ninjas.com/v1/exercises?muscle'
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

def get_all_exercises():
  return Exercise.query.all()

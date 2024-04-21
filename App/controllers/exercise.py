import requests, json 
from App.models import Exercise
from App.database import db

def parse_exercises():
    api_url = 'https://api.api-ninjas.com/v1/exercises?muscle'
    response = requests.get(api_url, headers={'X-Api-Key': '34ECD4LQjf7k/KSQABanUg==kRrodx9CuPCV9pAH'})
    exercises = json.loads(response.text)

    for i in exercises:
        exercise = Exercise(
            name = exercises[i]['name'],
            type = exercises[i]['type'],
            muscle = exercises[i]['muscle'],
            equipment = exercises[i]['equipment'],
            difficulty = exercises[i]['difficulty'],
            instructions = exercises[i]['instructions']
        )
        db.session.add(exercise)
    db.session.commit()
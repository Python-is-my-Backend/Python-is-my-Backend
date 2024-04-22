from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db
from App.controllers import create_user
from App.controllers.user import (create_routine, remove_routine, rename_routine)
index_views = Blueprint('index_views', __name__, template_folder='../templates')

from App.controllers.exercise import ( parse_exercises, find_exercises, get_all_exercises_by_muscle, get_all_exercises, get_exercise_by_id )

@index_views.route('/', methods=['GET'])
def index_page():
    init()
    return render_template('index.html')

@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    parse_exercises()
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})

@index_views.route('/home', methods=['GET'])
def home_page():
    routines = get_all_routines()
    return render_template("home.html", routines=routines)

@index_views.route('/exercises', methods=['GET'])
def list_exercises():
    exercises = get_all_exercises()
    return render_template("exercises.html", exercises=exercises)

@index_views.route('/add_routine/<int:exercise_id>', methods=['POST'])
def add_routine(exercise_id):
    data = request.form
    create_routine(exercise_id)
    return redirect(request.referrer)


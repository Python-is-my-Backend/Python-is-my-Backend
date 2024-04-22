from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db
from App.controllers import create_user

index_views = Blueprint('index_views', __name__, template_folder='../templates')

from App.controllers.exercise import ( parse_exercises, find_exercises, get_all_exercises_by_muscle, get_all_exercises )

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
    return render_template("home.html")

@index_views.route('/exercises', methods=['GET'])
def list_exercises():
    exercises = get_all_exercises()
    return render_template("exercises.html", exercises=exercises)

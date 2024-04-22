from App.models import Routine
from App.database import db

def get_all_routines():
  return Routine.query.all()
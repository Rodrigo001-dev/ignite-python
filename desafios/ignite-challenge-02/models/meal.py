from database import db
from flask_login import UserMixin

class Meal(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), nullable=False)
  description = db.Column(db.String(80), nullable=True)
  date = db.Column(db.String(80), nullable=False)
  is_in_diet = db.Column(db.Boolean, nullable=False, default=True)
  user_id = db.Column(db.Integer, nullable=False)
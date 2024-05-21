from flask import Flask, request, jsonify
from models.user import User
from models.meal import Meal
from database import db
import bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin123@0.0.0.0:3306/ignite-challenge-02'

db.init_app(app)

@app.route('/user', methods=["POST"])
def create_user():
  data = request.json
  username = data.get("username")
  password = data.get("password")

  if username and password:
    hashed_password = bcrypt.hashpw(str.encode(password), bcrypt.gensalt())
    user = User(username=username, password=hashed_password, role="user")

    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "Usuario cadastrado com sucesso"})

  return jsonify({"message": "Dados invalidos"}), 400

@app.route('/meal/<int:user_id>', methods=["POST"])
def create_meal(user_id):
  user = User.query.get(user_id)

  if not user:
    return jsonify({"message": "Usuario não encontrado"}), 404
  
  data = request.json
  name = data.get("name")
  description = data.get("description")
  date = data.get("date")
  is_in_diet = data.get("is_in_diet")

  if name and description and date and is_in_diet:
    meal = Meal(name=name, description=description, date=date, is_in_diet=eval(is_in_diet), user_id=user.id)

    db.session.add(meal)
    db.session.commit()
    return jsonify({"message": f"Refeição do usuário {user.id} cadastrado com sucesso"})
  
  return jsonify({"message": "Dados invalidos"}), 400

@app.route('/meal/<int:meal_id>', methods=["PUT"])
def update_meal(meal_id):
  meal = Meal.query.get(meal_id)

  if not meal:
    return jsonify({"message": "Refeição não encontada"}), 404
  
  data = request.json
  name = data.get("name")
  description = data.get("description")
  date = data.get("date")
  is_in_diet = data.get("is_in_diet")

  if name:
    meal.name = name
  if description:
    meal.description = description
  if date:
    meal.date = date
  if is_in_diet:
    meal.is_in_diet = is_in_diet

  db.session.commit()

  return jsonify({"message": f"Refeição {meal.id} atualizado com sucesso"})

@app.route('/meal/<int:meal_id>', methods=["DELETE"])
def delete_meal(meal_id):
  meal = Meal.query.get(meal_id)

  if not meal:
    return jsonify({"message": "Refeição não encontada"}), 404
  
  db.session.delete(meal)
  db.session.commit()
  return jsonify({"message": f"Refeição {meal_id} deletada com sucesso"})

@app.route('/meals/<int:user_id>', methods=["GET"])
def fetch_meals(user_id):
  meals = Meal.query.filter_by(user_id=user_id).all()
  meals_list = []

  for meal in meals:
    output = {
      "id": meal.id,
      "name": meal.name,
      "description": meal.description,
      "date": meal.date,
      "is_in_diet": meal.is_in_diet,
      "user_id": meal.user_id
    }
    meals_list.append(output)
  
  return jsonify(meals_list)

@app.route('/meal/<int:meal_id>', methods=["GET"])
def get_meal(meal_id):
  meal = Meal.query.get(meal_id)

  if not meal:
    return jsonify({"message": "Refeição não encontada"}), 404
  
  output = {
    "id": meal.id,
    "name": meal.name,
    "description": meal.description,
    "date": meal.date,
    "is_in_diet": meal.is_in_diet,
    "user_id": meal.user_id
  }

  return jsonify(output)


if __name__ == '__main__':
  app.run(debug=True)
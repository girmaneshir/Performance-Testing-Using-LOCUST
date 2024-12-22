from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name}

# Create the database
with app.app_context():
    db.create_all()

# Home route
@app.route('/')
def home():
    return "Welcome to the User Management API!"

# CRUD Operations
@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.json
    new_user = User(name=user_data['name'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    return jsonify(user.to_dict()) if user else ('', 404)

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return ('', 404)
    
    data = request.json
    user.name = data.get('name', user.name)
    db.session.commit()
    return jsonify(user.to_dict())

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return ('', 404)
    
    db.session.delete(user)
    db.session.commit()
    return ('', 204)

@app.route('/users/sample', methods=['POST'])
def create_sample_users():
    sample_users = [
        {"id": 1, "name": "John Doe"},
        {"id": 2, "name": "Jane Smith"},
        {"id": 3, "name": "Alice Johnson"},
        {"id": 4, "name": "Bob Brown"},
        {"id": 5, "name": "Charlie Davis"},
        {"id": 6, "name": "Diana Prince"},
        {"id": 7, "name": "Ethan Hunt"},
        {"id": 8, "name": "Fiona Apple"},
        {"id": 9, "name": "George Washington"},
        {"id": 10, "name": "Hannah Montana"}
    ]

    for user_data in sample_users:
        new_user = User(name=user_data['name'])  # Use name only
        db.session.add(new_user)

    db.session.commit()
    return jsonify({"message": "Sample users added."}), 201

if __name__ == '__main__':
    app.run(debug=True)
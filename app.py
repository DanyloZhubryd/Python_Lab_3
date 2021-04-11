from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Bird(db.Model):
    __tablename__ = 'Bird'
    id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String(50), unique=True)
    mass_in_kg = db.Column(db.Integer, nullable=False)
    age_in_years = db.Column(db.Integer)
    is_migratory = db.Column(db.Boolean)

    def __init__(self, species, mass_in_kg, age_in_years, is_migratory):
        self.species = species
        self.mass_in_kg = mass_in_kg
        self.age_in_years = age_in_years
        self.is_migratory = is_migratory


class BirdSchema(ma.Schema):
    class Meta:
        fields = ('id', 'species', 'mass_in_kg', 'age_in_years', 'is_migratory')


bird_schema = BirdSchema()
birds_schema = BirdSchema(many=True)


# Create a bird
@app.route('/bird', methods=['POST'])
def add_bird():
    species = request.json['species']
    mass_in_kg = request.json['mass_in_kg']
    age_in_years = request.json['age_in_years']
    is_migratory = request.json['is_migratory']

    new_bird = Bird(species, mass_in_kg, age_in_years, is_migratory)
    db.session.add(new_bird)
    db.session.commit()

    return bird_schema.jsonify(new_bird)


# Get single bird
@app.route('/bird/<id>', methods=['GET'])
def get_bird(id):
    bird = Bird.query.get(id)
    return bird_schema.jsonify(bird)


# Get All birds
@app.route('/bird', methods=['GET'])
def get_birds():
    all_birds = Bird.query.all()
    result = birds_schema.dump(all_birds)
    return jsonify(result)


@app.route('/bird/<id>', methods=['PUT'])
def update_bird(id):
    bird = Bird.query.get(id)

    species = request.json['species']
    mass_in_kg = request.json['mass_in_kg']
    age_in_years = request.json['age_in_years']
    is_migratory = request.json['is_migratory']

    bird.species = species
    bird.mass_in_kg = mass_in_kg
    bird.age_in_years = age_in_years
    bird.is_migratory = is_migratory

    db.session.commit()

    return bird_schema.jsonify(bird)


# Delete single bird
@app.route('/bird/<id>', methods=['DELETE'])
def delete_bird(id):
    bird = Bird.query.get(id)
    db.session.delete(bird)
    db.session.commit()
    return bird_schema.jsonify(bird)


if __name__ == '__main__':
    app.run(debug=True)

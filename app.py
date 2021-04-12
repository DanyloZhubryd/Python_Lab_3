from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields
# Init app
app = Flask(__name__)
# Database
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'mysql+mysqlconnector://myuser:aboba@localhost:3306/Lab6'
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Bird(db.Model):
    __tablename__ = 'bird'
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

    def update(self, species, mass_in_kg, age_in_years, is_migratory):
        self.__init__(species, mass_in_kg, age_in_years, is_migratory)


def get_bird_by_id(id):
    bird = Bird.query.get(id)
    if not bird:
        return abort(404)
    return bird


class BirdSchema(ma.Schema):
    species = fields.String()
    mass_in_kg = fields.Integer()
    age_in_years = fields.Integer()
    is_migratory = fields.Boolean()


bird_schema = BirdSchema()
birds_schema = BirdSchema(many=True)


# Create a bird
@app.route('/bird', methods=['POST'])
def add_bird():
    fields = bird_schema.load(request.json)
    new_bird = Bird(**fields)
    db.session.add(new_bird)
    db.session.commit()

    return bird_schema.jsonify(new_bird)


# Get single bird
@app.route('/bird/<id>', methods=['GET'])
def get_bird(id):
    bird = get_bird_by_id(id)
    return bird_schema.jsonify(bird)


# Get All birds
@app.route('/bird', methods=['GET'])
def get_birds():
    all_birds = Bird.query.all()
    if not all_birds:
        return abort(404)
    result = birds_schema.dump(all_birds)
    return birds_schema.jsonify(result)


# Update Single bird
@app.route('/bird/<id>', methods=['PUT'])
def update_bird(id):
    bird = get_bird_by_id(id)
    fields = bird_schema.load(request.json)
    bird.update(**fields)

    db.session.commit()
    return bird_schema.jsonify(bird)


# Delete single bird
@app.route('/bird/<id>', methods=['DELETE'])
def delete_bird(id):
    bird = get_bird_by_id(id)
    db.session.delete(bird)
    db.session.commit()
    return bird_schema.jsonify(bird)


if __name__ == '__main__':
    app.run(debug=True)

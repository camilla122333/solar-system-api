from flask import Blueprint, jsonify, make_response, abort
# Define a Planet class with the attributes id, name,
# and description, and one additional attribute
# Create a list of Planet instances

class Planet():
    def __init__(self, id, name, description, moons):
        self.id = id
        self.name = name
        self.description = description
        self.moons = moons

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "moons": self.moons
        }

planets = [
    Planet(1, "Mercury", ["red", "hot"], False),
    Planet(2, "Venus", ["orange", "hot"], False),
    Planet(3, "Earth", ["blue", "hot"], True)
]

# planet_bp = Blueprint("planet_bp", __name__)
planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

#Get all planets
@planet_bp.route("", methods=["GET"])
def read_all_planets():
    planets_response = []

    for planet in planets:
        planets_response.append(planet.to_json())

    return jsonify(planets_response)

'''
Create the following endpoint(s), with similar functionality
presented in the Hello Books API:

As a client, I want to send a request...
...to get one existing planet, so that I can see the id, name, description,
and other data of the planet.
... such that trying to get one non-existing planet responds
with get a 404 response, so that I know the planet resource was not found.
... such that trying to get one planet with an invalid planet_id responds
with get a 400 response, so that I know the planet_id was invalid.
'''

def validate_planet(id):
    try:
        id = int(id)
    except:
        return abort(make_response({"message": f"planet {id} is invalid"}, 400))

    for planet in planets:
        if planet.id == id:
            return planet

    return abort(make_response({"message": f"planet {id} is not found"}, 404))

#Get one planet
@planet_bp.route("/<id>", methods=["GET"])
def read_one_planet(id):
    planet = validate_planet(id)

    return jsonify(planet.to_json(), 200)


'''
def validate_cat(id):
    try:
        id = int(id)
    except:
        return abort(make_response({"message": f"cat {id} is invalid"}, 400))

    for cat in cats:
        if cat.id == id:
            return cat

    return abort(make_response({"message":f"cat {id} not found"}, 404))

'''
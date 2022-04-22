from flask import Blueprint, jsonify
# Define a Planet class with the attributes id, name,
# and description, and one additional attribute
# Create a list of Planet instances

class Planet():
    def __init__(self, id, name, description, moons):
        self.id = id
        self.name = name
        self.description = description
        self.moons = moons

planets = [
    Planet( 1, "Mercury", ["red", "hot"], False),
    Planet( 2, "Venus", ["orange", "hot"], False),
    Planet( 3, "Earth", ["blue", "hot"], True)
]

planet_bp = Blueprint("planet", __name__, url_prefix="/planets")

#Get all planets
@planet_bp.route("", methods=["GET"])
def read_all_planets():
    planets_response = []

    for planet in planets:
        planets_response.append(planet.to_json())

    return jsonify(planets_response)


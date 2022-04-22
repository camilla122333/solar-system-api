from flask import Blueprint
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


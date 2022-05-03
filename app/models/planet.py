from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    moons = db.Column(db.Boolean, nullable=False)


    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "moons": self.moons
        }

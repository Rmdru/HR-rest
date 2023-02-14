from __main__ import SQLAlchemy, db

# Define the Lesson model
class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(200), nullable=False)
    start_time = db.Column(db.String(200), nullable=False)
    end_time = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'date': self.date,
            'start_time': self.start_time,
            'end_time': self.end_time
        }
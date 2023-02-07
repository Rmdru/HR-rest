from __main__ import SQLAlchemy

# Initialize the database
db = SQLAlchemy()


# Define the Lesson model
class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'))
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(200), nullable=False)
    time = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Lesson {self.id}: {self.name}>'
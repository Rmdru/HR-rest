from __main__ import SQLAlchemy, db, app
from sqlalchemy.orm import relationship

# Define the Lesson model
class Lesson(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    question = db.Column(db.String(600), nullable=True)
    date = db.Column(db.String(200), nullable=False)
    start_time = db.Column(db.String(200), nullable=False)
    end_time = db.Column(db.String(200), nullable=False)

    attendance_records = relationship('Attendance', backref='lesson_record', cascade='all, delete')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'question': self.question,
            'date': self.date,
            'start_time': self.start_time,
            'end_time': self.end_time,
        }

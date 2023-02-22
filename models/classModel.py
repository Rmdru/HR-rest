from __main__ import SQLAlchemy, db

# Define the Class model
class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
 
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
         }


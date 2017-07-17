from flask_sqlalchemy import SQLAlchemy
from . import db

class Organization(db.Model):
    __tablename__ = 'organizations'
    name = db.Column(db.String(64), primary_key=True)

    def __repr__(self):
        return '<Organization %r>' % self.name
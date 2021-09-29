from app.configs.database import db
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Leads(db.Model):
    id: int
    name: str
    email: str
    phone: str
    creation_date: datetime
    last_visit: datetime
    visits: int

    __tablename__ = "lead"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    phone = db.Column(db.String, nullable=False, unique=True)
    creation_date = db.Column(db.Datetime, default=datetime.utcnow())
    last_visit = db.Column(db.Datetime, default=datetime.utcnow())
    visits = db.Column(db.Integer, default=1)

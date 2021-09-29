import re
from dataclasses import dataclass
from datetime import datetime

from app.configs.database import db
from app.exc.lead_exc import InvalidNumberPhoneError
from sqlalchemy.orm import validates


@dataclass
class Leads(db.Model):
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
    creation_date = db.Column(db.Date, default=datetime.utcnow())
    last_visit = db.Column(db.Date, default=datetime.utcnow())
    visits = db.Column(db.Integer, default=1)

    @validates("phone")
    def validate_phone(self, key, phone):
        success = re.fullmatch(r"^\(?\d{2}\)?[\s-]?[\s9]?\d{4}-?\d{4}$", phone)
        if not success:
            raise InvalidNumberPhoneError("Incorrect number.")

        return phone

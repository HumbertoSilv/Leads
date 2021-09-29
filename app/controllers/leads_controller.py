import sqlalchemy
from app.exc.lead_exc import InvalidNumberPhoneError
from app.models.leads_model import Leads
from flask import current_app, jsonify, request


def register_lead():
    data = request.json

    try:
        new_lead = Leads(**data)
        current_app.db.session.add(new_lead)
        current_app.db.session.commit()
        return jsonify(new_lead), 201

    except sqlalchemy.exc.IntegrityError as e:
        return {"msg": str(e).split("\n")[1]}, 409

    except InvalidNumberPhoneError as e:
        return {"msg": str(e)}, 400


def get_leads():
    ...


def update_lead():
    ...


def delete_lead():
    ...

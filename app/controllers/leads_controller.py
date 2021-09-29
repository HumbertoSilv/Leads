import sqlalchemy
from app.exc.lead_exc import InvalidNumberPhoneError
from app.models.leads_model import Leads
from flask import current_app, jsonify, request
from datetime import datetime


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
    try:
        all_leads = Leads.query.order_by(Leads.visits).all()
        return jsonify(all_leads), 200

    except sqlalchemy.exc.ProgrammingError:
        return {"msg": "No data found."}, 404


def update_lead():
    data = request.json
    if type(data["email"]) != str:
        return {"msg": "Format Email invalid."}

    user = Leads.query.filter_by(email=data["email"]).first_or_404()
    user.visits += 1
    user.last_visit = datetime.utcnow()

    current_app.db.session.add(user)
    current_app.db.session.commit()

    return {}, 204


def delete_lead():
    ...

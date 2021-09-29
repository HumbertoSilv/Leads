from flask import request, jsonify, current_app
from app.models.leads_model import Leads


def register_lead():
    data = request.json

    new_lead = Leads(**data)
    current_app.db.session.add(new_lead)
    current_app.db.session.commit()

    return jsonify(new_lead), 201


def get_leads():
    ...


def update_lead():
    ...


def delete_lead():
    ...

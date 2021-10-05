from datetime import datetime

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

    except TypeError:
        return {
            "msg": "The fields name, email and phone must be informed."
            }, 400


def get_leads():
    try:
        all_leads = Leads.query.order_by(Leads.visits).all()
        return jsonify(all_leads), 200

    except sqlalchemy.exc.ProgrammingError:
        return {"msg": "No data found."}, 404


def update_lead():
    data = request.json
    try:
        if type(data["email"]) != str:
            return {"msg": "Format Email invalid."}, 400

        if len(data) > 1:
            return {"msg": "Number of fields higher than expected."}, 400

        user = Leads.query.filter_by(email=data["email"]).first_or_404()
        user.visits += 1
        user.last_visit = datetime.utcnow()

        current_app.db.session.add(user)
        current_app.db.session.commit()
        return {}, 204

    except KeyError as e:
        return {"msg": f"Missing {e} field"}, 400

    except TypeError:
        return {"msg": "The e-mail field must be informed."}, 400


def delete_lead():
    data = request.json
    try:
        if len(data) > 1:
            return {"msg": "Number of fields higher than expected."}, 400

        if type(data["email"]) != str:
            return {"msg": "Format Email invalid."}, 400

        user = Leads.query.filter_by(email=data["email"]).first_or_404()

        current_app.db.session.delete(user)
        current_app.db.session.commit()
        return {}, 204

    except KeyError as e:
        return {"msg": f"Missing {e} field"}, 400

    except TypeError:
        return {"msg": "The e-mail field must be informed."}, 400

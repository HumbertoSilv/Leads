from flask import Blueprint
from app.controllers.leads_controller import (
    update_lead, get_leads, register_lead, delete_lead
)

bp = Blueprint("lead_bp", __name__, url_prefix="/api")


bp.post("lead")(register_lead)
bp.get("lead")(get_leads)
bp.patch("lead")(update_lead)
bp.delete("lead")(delete_lead)

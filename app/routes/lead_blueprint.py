from flask import Blueprint
from app.controllers.leads_controller import (
    update_lead, get_leads, register_lead, delete_lead
)

bp = Blueprint("lead_bp", __name__, url_prefix="/lead")


bp.post("")(register_lead)
bp.get("")(get_leads)
bp.patch("")(update_lead)
bp.delete("")(delete_lead)

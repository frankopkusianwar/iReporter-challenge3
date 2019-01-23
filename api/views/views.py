from flask import Blueprint, request, jsonify
from api.controllers.userController import UserController
from api.controllers.incidentController import IncidentController
from functools import wraps
import jwt

bp = Blueprint("ireporterViews", __name__, url_prefix="/api/v2")
incident = IncidentController()
user = UserController()


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({"message": "token missing"}), 401
        try:
            data = jwt.decode(token, 'franko@pkusianwar')
            current_user = user.get_spec_user(data['userId'])
        except:
            return jsonify({"message": "invalid token"})
        return f(current_user, *args, **kwargs)
    return decorated


@bp.route("/users", methods=["POST"])
def createUser():
    return user.create_user()


@bp.route("/red-flags", methods=["GET", "POST"])
# @token_required
def createIncident():
    if request.method == 'POST':
        return incident.create_incident()
    else:
        return incident.get_all_incident()

@bp.route("/interventions", methods=["GET"])
# @token_required
def get_all_interventions():
    return incident.get_all_interventions()

@bp.route("/red-flags/<int:red_flag_id>", methods=["GET", "DELETE"])
# @token_required
def SpecificIncidents(red_flag_id):
    if request.method == 'GET':
        return incident.get_one_incident(red_flag_id)
    else:
        return incident.delete_one_incident(red_flag_id)

@bp.route("/interventions/<int:intervention_id>", methods=["GET", "DELETE"])
# @token_required
def SpecificInterventions(intervention_id):
    if request.method == 'GET':
        return incident.get_one_intervention(intervention_id)
    else:
        return incident.delete_one_intervention(intervention_id)

@bp.route("/red-flags/<int:location_incident_id>/location", methods=["PATCH"])
# @token_required
def edit_specific_incident_location(location_incident_id):
    return incident.update_particular_location(location_incident_id)


@bp.route("/interventions/<int:location_incident_id>/location", methods=["PATCH"])
# @token_required
def edit_specific_intervention_location(location_incident_id):
    return incident.update_intervention_location(location_incident_id)


@bp.route("/red-flags/<int:comment_incident_id>/comment", methods=["PATCH"])
# @token_required
def add_comment_to_specific_red_flag_record(comment_incident_id):
    return incident.create_comment(comment_incident_id)

@bp.route("/intervention/<int:comment_incident_id>/comment", methods=["PATCH"])
# @token_required
def add_comment_to_specific_intervention_record(comment_incident_id):
    return incident.create_intervention_comment(comment_incident_id)


@bp.route("/red-flags/<int:status_incident_id>/status", methods=["PATCH"])
# @token_required
def change_red_flag_status(status_incident_id):
    return incident.change_particular_status(status_incident_id)

@bp.route("/intervention/<int:status_incident_id>/status", methods=["PATCH"])
# @token_required
def change_intervention_status(status_incident_id):
    return incident.change_particular_status(status_incident_id)


@bp.route("/login", methods=["GET"])
def login_user():
    return user.login()

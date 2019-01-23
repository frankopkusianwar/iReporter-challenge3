from flask import Blueprint, request, jsonify
from api.controllers.userController import UserController
from api.controllers.incidentController import IncidentController
from functools import wraps
import jwt

bp = Blueprint("ireporterViews", __name__, url_prefix="/api/v1")
incident = IncidentController()
user = UserController()

def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({"message":"token missing"}),401
        try:
            data = jwt.decode(token, 'franko@pkusianwar')
            current_user = user.get_spec_user(data['userId'])
        except:
            return jsonify({"message":"invalid token"})
        return f(current_user,*args,**kwargs)
    return decorated

@bp.route("/users", methods=["POST"])
def createUser():
    return user.create_user()

@bp.route("/red-flags", methods=["GET","POST"])
@token_required
def redFlags(current_user):
    if request.method == 'POST':
        return incident.create_incident()
    else:
        return incident.get_all_incident()

@bp.route("/red-flags/<int:red_flag_id>", methods=["GET","DELETE"])
@token_required
def SpecificIncidents(current_user, red_flag_id):
    if request.method == 'GET':
        return incident.get_one_incident(red_flag_id)
    else:
        return incident.delete_one_incident(red_flag_id)

@bp.route("/red-flags/<int:location_incident_id>/location", methods=["PATCH"])
@token_required
def edit_specific_incident_location(current_user, location_incident_id):
    return incident.update_particular_location(location_incident_id)

@bp.route("/red-flags/<int:comment_incident_id>/comment", methods=["PATCH"])
@token_required
def add_comment_to_specific_red_flag_record(current_user, comment_incident_id):
    return incident.create_comment(comment_incident_id)

@bp.route("/red-flags/<int:status_incident_id>/status", methods=["PATCH"])
@token_required
def change_red_flag_status(current_user, status_incident_id):
    return incident.change_particular_status(status_incident_id)

@bp.route("/login", methods=["GET"])
def login_user():
    return user.login()
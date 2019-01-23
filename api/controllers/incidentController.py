from flask import request, jsonify
from api.models.db import DatabaseConnection
from api.utilities import check_inc
import uuid
import datetime

db = DatabaseConnection()


class IncidentController:
    def create_incident(self):
        incident_data = request.get_json()
        incident_type = incident_data.get('incidentType')
        location = incident_data.get('location')
        status = "draft"
        created_on = datetime.datetime.today()
        created_by = request.headers["userId"]
        images = incident_data.get('images')
        videos = incident_data.get('videos')
        comment = ""

        validate_fields = [location, images, videos]
        if check_inc(validate_fields, location, images, videos) == "invalid":
            return jsonify({"status": 400, "message": "please fill all fields"}), 400
        if incident_type != "red-flag" and incident_type != "intervention":
            return jsonify({"status": 400, "message": "please enter incidentType as red-flag or intervention"}), 400

        db.insert_incident(incident_type, location, status,
                           images, videos, created_by, comment, created_on)

        return jsonify({
            "data": [{
                "status": 201,
                "message": "created red-flag record",
            }]
        }), 201

    def get_all_incident(self):
        if db.get_all_incidents() == None:
            return jsonify({"status": 200, "message": "red-flag records not found"})
        return jsonify({
            "status": 200,
            "data": db.get_all_incidents()
        })

    def get_all_interventions(self):
        if db.get_all_interventions() == None:
            return jsonify({"status": 200, "message": "intervention records not found"})
        return jsonify({
            "status": 200,
            "data": db.get_all_interventions()
        })

    def get_one_incident(self, particular_id):
        if db.get_one_incident(particular_id) == None:
            return jsonify({"status": 200, "message": "requested red-flag-id not found"})
        return jsonify({
            "status": 200,
            "data": [db.get_one_incident(particular_id)]
        })

    def get_one_intervention(self, particular_id):
        if db.get_one_intervention(particular_id) == None:
            return jsonify({"status": 200, "message": "requested intervention-id not found"})
        return jsonify({
            "status": 200,
            "data": [db.get_one_intervention(particular_id)]
        })

    def create_comment(self, comment_id):
        comment_data = request.get_json()
        new_comment = comment_data.get("comment")
        db.edit_comment(comment_id, new_comment)
        if db.edit_comment(comment_id, new_comment) == None:
            return jsonify({"status": 200, "message": "the red-flag you're trying to comment on  does not exist"})
        return jsonify({
            "data": [{
                "status": 200,
                "message": "updated red-flag record's comment"
            }]
        })

    def create_intervention_comment(self, comment_id):
        comment_data = request.get_json()
        new_comment = comment_data.get("comment")
        db.edit_intervention_comment(comment_id, new_comment)

        return jsonify({
            "data": [{
                "status": 200,
                "message": "updated intervention record's comment"
            }]
        })

    def update_particular_location(self, location_id):
        location_data = request.get_json()
        new_location = location_data.get("location")
        db.edit_location(location_id, new_location)
        return jsonify({
            "data": [{
                "status": 200,
                "message": "updated red-flag record's location"
            }]
        })

    def update_intervention_location(self, location_id):
        location_data = request.get_json()
        new_location = location_data.get("location")
        db.edit_intervention_location(location_id, new_location)
        return jsonify({
            "data": [{
                "status": 200,
                "message": "updated red-flag record's location"
            }]
        })

    def change_particular_status(self, status_id):
        status_data = request.get_json()
        new_status = status_data.get("status")
        db.edit_status(status_id, new_status)
        return jsonify({
            "status": 200,
            "message": "status updated successfully"
        })

    def change_intervention_status(self, status_id):
        status_data = request.get_json()
        new_status = status_data.get("status")
        db.edit_intervention_status(status_id, new_status)
        return jsonify({
            "status": 200,
            "message": "status updated successfully"
        })

    def delete_one_incident(self, delete_id):
        db.delete_incident(delete_id)
        return jsonify({
            "data": [{
                "status": 200,
                "message": "red-flag record has been deleted"
            }]
        })

    def delete_one_intervention(self, delete_id):
        db.delete_intervention(delete_id)
        return jsonify({
            "data": [{
                "status": 200,
                "message": "red-flag record has been deleted"
            }]
        })

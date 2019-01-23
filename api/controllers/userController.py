from flask import request, jsonify
#from api.models.models import User, IreporterDb
from api.utilities import check_user, check_email, check_paswd
import uuid
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from api.models.db import DatabaseConnection
import jwt

db = DatabaseConnection()


class UserController:
    def create_user(self):
        user_data = request.get_json()
        first_name = user_data.get('firstName')
        last_name = user_data.get('lastName')
        other_names = user_data.get('otherNames')
        username = user_data.get('username')
        email = user_data.get('email')
        password = generate_password_hash(
            user_data.get('password'), method='sha256')
        registered = datetime.datetime.today()
        is_admin = False
        public_user_id = str(uuid.uuid4())

        validate_user = [first_name, last_name,
                         other_names, username, email, password]
        if check_user(validate_user) == "invalid":
            return jsonify({
                "status": 400,
                "message": "please fill all fields"
            }), 400

        if check_email(email) == "invalid":
            return jsonify({
                "status": 400,
                "message": "invalid email adress"
            }), 400

        if check_paswd(password) == "invalid":
            return jsonify({
                "status": 400,
                "message": "password should be more than 8 characters"
            }), 400

        hashed_password = generate_password_hash(
            user_data.get('password'), method='sha256')
        db.insert_user(first_name, last_name, other_names,
                       username, email, password, is_admin, registered)

        return jsonify({
            "data": [{
                "status": 201,
                "message": "user created successfully",
            }]
        }), 201

    def login(self):
        auth = request.authorization
        if not auth.username or not auth.password:
            return jsonify({"message": "please enter username and password"}), 401
        user_check = [db.login(auth.username)]
        if check_password_hash(user_check[0]['password'], auth.password):
            access_token = jwt.encode({"userId": user_check[0]['username'], "exp": datetime.datetime.utcnow(
            ) + datetime.timedelta(minutes=30)}, "franko@pkusianwar")

            return jsonify({'access-token': access_token.decode('UTF-8')})
        return jsonify({"message": "invalid password"}), 401

    """def get_spec_user(self, particular_id):
        return jsonify({
            "status": 200,
            "data": new_user.get_specific_user(particular_id)
        }) """

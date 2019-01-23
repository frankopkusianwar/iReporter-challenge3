import unittest
from api.models.db import DatabaseConnection
from flask import request
import json
from tests.base import BaseTest

class TestUsers(BaseTest):
    
    def test_create_user(self):
        user = {"firstName":"ofgh", "lastName":"franko", "otherNames":"oki", "username":"francis", "email":"jrfgmugabe@gmail.com",
        "password":"23435354646", "isAdmin":False, "registered":"2019-01-20"}
        response = self.test_client.post(
            'api/v1/users',
            content_type='application/json',
            data=json.dumps(user)
        )
        message = json.loads(response.data)
        self.assertEqual(message['data'][0]['message'],
                         'user created successfully')
        self.assertEqual(response.status_code,
                         201)

    def test_user_empty_fields(self):
        user = {"firstName":"ofgh", "":"franko", "":"oki", "username":"francis", "email":"jrfgmugabe@gmail.com",
        "password":"", "isAdmin":False, "registered":"2019-01-20"}
        response = self.test_client.post(
            'api/v1/users',
            content_type='application/json',
            data=json.dumps(user)
        )
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         'please fill all fields')

    def test_for_valid_email(self):
        user = {"firstName":"ofgh", "lastName":"franko", "otherNames":"oki", "username":"francis", "email":"jrfgmugabcom",
        "password":"23435354646", "isAdmin":False, "registered":"2019-01-20"}
        response = self.test_client.post(
            'api/v1/users',
            content_type='application/json',
            data=json.dumps(user)
        )
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         'invalid email adress')

    def test_check_password_length(self):
        user = {"firstName":"ofgh", "lastName":"franko", "otherNames":"oki", "username":"francis", "email":"jrfgmugabe@gmail.com",
        "password":"234", "isAdmin":False, "registered":"2019-01-20"}
        response = self.test_client.post(
            'api/v1/users',
            content_type='application/json',
            data=json.dumps(user)
        )
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         'password should be more than 8 characters')       
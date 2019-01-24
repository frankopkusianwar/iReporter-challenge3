from flask import request
import json
from tests.base import BaseTest


class TestEndpoints(BaseTest):
    
    def test_create_incident(self):
        incident = {"incidentType":"red-flag", "location":"120.00", "status":"draft", "images":'image-url', "videos":"video-url","createdBy": 2, "comment":"", "created_on":"25-nov-2018"}
        response = self.test_client.post(
            'api/v1/red-flags',
            content_type='application/json',
            data=json.dumps(incident),
            headers=self.token()
        )
        message = json.loads(response.data.decode())
        self.assertEqual(message['data'][0]['message'],
                         'created red-flag record')

'''    def test_check_invalid_incident_type(self):
        incident = {"incidentType":"relag", "location":"120.00", "status":"draft", "images":'image-url', "videos":"video-url","createdBy": 2, "comment":"", "created_on":"25-nov-2018"}
        response = self.test_client.post(
            'api/v1/red-flags',
            content_type='application/json',
            data=json.dumps(incident),
            headers={"userId": 2}
        )
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         'please enter incidentType as red-flag or intervention')

    def test_check_empty_incident_fields(self):
        incident = {"incidentType":"", "location":"", "status":"", "images":"", "videos":"video-url","createdBy": 2, "comment":"", "created_on":"25-nov-2018"}
        response = self.test_client.post(
            'api/v1/red-flags',
            content_type='application/json',
            data=json.dumps(incident),
            headers={"userId": 2}
        )
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         'please fill all fields')

    def test_get_all_incidents(self):
        response = self.test_client.get('api/v1/red-flags')
        message = json.loads(response.data.decode())
        self.assertEqual(message['status'],
                         200)
                         
    #check for getting single red-flag record                     
    def test_get_single_red_flag(self):
        response = self.test_client.get('api/v1/red-flags/{}'.format(1))
        message = json.loads(response.data.decode())
        self.assertEqual(message['status'],
                         200)

    #test whether a comment is added osuccessfully
    def test_add_comment_to_red_flag(self): 
        response = self.test_client.patch('api/v1/red-flags/{}/comment'.format(1), content_type='application/json', data=json.dumps({"comment":"this is a comment"}))
        message = json.loads(response.data.decode())
        self.assertEqual(message['data'][0]['message'],
                         "updated red-flag record's comment")

    def test_update_location(self):
        resp = self.test_client.patch('api/v1/red-flags/{}/location'.format(1), content_type='application/json', data=json.dumps({"location": "13.00"}))
        assert(resp.status_code) == 200
        message = json.loads(resp.data.decode())
        self.assertEqual(message['data'][0]['message'],
                         "updated red-flag record's location")

    def test_update_status(self):
        resp = self.test_client.patch('api/v1/red-flags/{}/status'.format(1), content_type='application/json', data=json.dumps({"location":"resolved"}))
        assert(resp.status_code) == 200
        message = json.loads(resp.data.decode())
        self.assertEqual(message['message'],
                         'status updated successfully')

    def test_delete_red_flag(self):
        response = self.test_client.delete('api/v1/red-flags/{}'.format(2))
        message = json.loads(response.data.decode())
        self.assertEqual(message['data'][0]['message'],
                         'red-flag record has been deleted')

    #check for a red-flag id that does not exist
    def test_check_specific_red_flag_does_not_exist(self): 
        response = self.test_client.get('api/v1/red-flags/{}'.format(2))
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         'requested red-flag-id not found') '''

'''    def test_add_comment_id_does_not_exist(self): 
        response = self.test_client.patch('api/v1/red-flags/{}/comment'.format(2), content_type='application/json', data=json.dumps({"comment":"this is a comment"}))
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         "the red-flag you're trying to comment on  does not exist") '''

'''    def test_check_delete_id_does_not_exist(self):
        response = self.test_client.delete('api/v1/red-flags/{}'.format(2))
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         'the id to delete does not exist or status is under investigation, rejected, or resolved') '''

'''    def test_update_location_id_does_not_exist(self):
        resp = self.test_client.patch('api/v1/red-flags/{}/location'.format(2), content_type='application/json', data=json.dumps({"location":{"latitude":"13.00","longitude":"13.00"}}))
        assert(resp.status_code) == 200
        message = json.loads(resp.data.decode())
        self.assertEqual(message['message'],
                         'the id does not exist or status is under investigation, rejected, or resolved')

    def test_update_status_id_does_not_exist(self):
        resp = self.test_client.patch('api/v1/red-flags/{}/status'.format(2), content_type='application/json', data=json.dumps({"location":"resolved"}))
        assert(resp.status_code) == 200
        message = json.loads(resp.data.decode())
        self.assertEqual(message['message'],
                         "the red-flag you're trying to change status does not exist") '''                  
    
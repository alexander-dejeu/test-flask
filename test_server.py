import API_services_code_challenges as server
import unittest
from flask import Flask, request, json



class FlaskServerTest(unittest.TestCase):

    def setUp(self):
        # Run app in testing mode to retrieve excpetions and stack traces
        server.app.testing = True
        self.app = server.app.test_client()

    # def test_hello(self):
    #     response = self.app.get('/hello')
    #     self.assertEqual(response.status_code, 200)
    #     assert response.status_code == 200, 'status_code was not OK'
    #     assert response.data == 'Hello World!'

    def test_post_pet(self):
        response= self.app.post('/pets',
                       data= json.dumps([{'name': 'Alex'}, {'age': '14'}, {'species': 'human'}]),
                       content_type= 'application/json')
        response_dict = json.loads(response)
        expected_dict = json.dumps({'name': 'Alex'}, {'age': '14'}, {'species': 'human'})
        self.assertEqual(response_dict, expected_dict)

    def test_hello_to_person(self):
        response = self.app.get('/hello/Alex')
        assert response.data == 'Hello, Alex!'

if __name__ == '__main__':
    unittest.main()

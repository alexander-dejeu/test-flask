import API_services_code_challenges as server
import unittest


class FlaskServerTest(unittest.TestCase):

    def setUp(self):
        # Run app in testing mode to retrieve excpetions and stack traces
        server.app.testing = True
        self.app = server.app.test_client()

    def test_hello(self):
        response = self.app.get('/hello')
        self.assertEqual(response.status_code, 200)
        assert response.status_code == 200, 'status_code was not OK'
        assert response.data == 'hello, world'

    def test_hello_to_person(self):
        response = self.app.get('/hello/Alex')
        assert response.data == 'Hello, Alex!'

if __name__ == '__main__':
    unittest.main()

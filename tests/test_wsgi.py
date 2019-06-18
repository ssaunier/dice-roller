from flask_testing import TestCase
from wsgi import app

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_one_roll(self):
        roll = self.client.get('/').json['roll']
        self.assertIsInstance(roll, int)
        self.assertGreater(roll, 0)
        self.assertLess(roll, 7)

import unittest
from app import app

class Testhello(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status,'200 OK')
        self.assertEqual(rv.data,b"HELLO WORLD \n")

if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output = 'test-reports')
    unittest.main(testRunner = runner)

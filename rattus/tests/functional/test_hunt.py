from rattus.tests import *

class TestHuntController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='hunt', action='index'))
        # Test response...

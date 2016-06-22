from unittest import TestCase

import futs

class TestJoke(TestCase):
    def test_is_string(self):
        s = futs.joke()
        self.assertTrue(isinstance(s, basestring))

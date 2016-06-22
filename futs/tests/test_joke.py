from unittest import TestCase

import robs_tool_belt

class TestJoke(TestCase):
    def test_is_string(self):
        s = robs_tool_belt.joke()
        self.assertTrue(isinstance(s, basestring))

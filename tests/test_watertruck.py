#! /usr/bin/env python3

try:
    from unittest import mock
except ImportError:
    import mock

import json
import unittest

import bikeshed

class GetColorTests(unittest.TestCase):
    def setUp(self):
        bikeshed.service.testing = True
        self.service = bikeshed.service.test_client()
        self.uri = "/{}/color".format(bikeshed.__version__)

    @mock.patch("bikeshed.sample", lambda x, y: (0, 0, 0))
    def test_black(self):
        """Given black RGB values, ensure we get the expected black hex."""
        response = self.service.get(self.uri)
        values = json.loads(response.get_data().decode("utf8"))
        self.assertEqual(values["hex"], "#000000")

    @mock.patch("bikeshed.sample", lambda x, y: (255, 255, 255))
    def test_white(self):
        """Given white RGB values, ensure we get the expected white hex."""
        response = self.service.get(self.uri)
        values = json.loads(response.get_data().decode("utf8"))
        self.assertEqual(values["hex"], "#FFFFFF")


if __name__ == "__main__":
    unittest.main()


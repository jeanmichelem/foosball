"""Testing file for TestDB.py"""

import unittest
import db
from models import Player

class TestDB(unittest.TestCase):
    """Tests for database file functions"""

    database_name = None

    @classmethod
    def setup_class(cls):
        """Connect to database"""
        db.database_connect()

    @classmethod
    def teardown_class(cls):
        # TODO: drop db
        pass

    def test_find(self):
        Player.create({'name': 'test', 'surname': 'test'})
        players = Player.find()
        self.assertGreater(len(players), 0, "Players array should be greater than zero")

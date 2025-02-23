import unittest
from src.services.wine_details import WineDetails

class WineDetailsTest(unittest.TestCase):
    def setUp(self):
        self.wine_details = WineDetails()

    def test_get_details(self):
        details = self.wine_details.get_details("Vinho Tinto A")
        self.assertIsNotNone(details)
        self.assertEqual(details["name"], "Vinho Tinto A")
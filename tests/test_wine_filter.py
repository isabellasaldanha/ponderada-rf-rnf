import unittest
from src.services.wine_filter import WineFilter

class WineFilterTest(unittest.TestCase):
    def setUp(self):
        self.wine_filter = WineFilter()

    def test_filter_by_type(self):
        filtered_wines = self.wine_filter.filter_by_type("tinto")
        self.assertTrue(all(wine["type"] == "tinto" for wine in filtered_wines))

    def test_filter_by_price_range(self):
        filtered_wines = self.wine_filter.filter_by_price_range(45, 55)
        self.assertTrue(all(45 <= wine["price"] <= 55 for wine in filtered_wines))
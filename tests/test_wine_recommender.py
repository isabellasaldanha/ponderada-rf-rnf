import unittest
from src.services.wine_recommender import WineRecommender

class WineRecommenderTest(unittest.TestCase):
    def setUp(self):
        self.wine_recommender = WineRecommender()

    def test_get_recommendations(self):
        recommendations = self.wine_recommender.get_recommendations()
        self.assertGreater(len(recommendations), 0)
        self.assertIn("reason", recommendations[0])
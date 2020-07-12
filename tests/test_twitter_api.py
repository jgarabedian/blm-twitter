import unittest
from unittest import TestCase

from TwitterClient import TwitterClient


class TwitterClientTest(TestCase):
    def test_api(self):
        api = TwitterClient()
        geocode = "38.9072,-77.0369,50km"
        tweets = api.get_tweets(query="blm", count=10,
                                geocode=geocode, city='Washington, DC')
        num_tweets = len(tweets)
        self.assertGreater(num_tweets, 0, msg="Bringing in tweets works")


if __name__ == '__main__':
    unittest.main()

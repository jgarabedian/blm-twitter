import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer


class TwitterClient(object):
    def __init__(self):
        try:
            import os
            consumer_key = os.environ.get("CONSUMER_KEY")
            consumer_secret = os.environ.get("CONSUMER_SECRET")
            access_token = os.environ.get("ACCESS_TOKEN")
            access_secret = os.environ.get("ACCESS_SECRET")

            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_secret)
            self.api = tweepy.API(self.auth)
        except:
            print("Authentication error")

    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w+:\ / \ / \S+)", " ", tweet).split())

    def get_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet), analyzer=NaiveBayesAnalyzer())
        if analysis.polarity > 0:
            return "positive"
        elif analysis.polarity == 0:
            return "neutral"
        else:
            return "negative"

    def get_polarity(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        # ramp up the intensity
        return analysis.polarity * 2

    def get_tweets(self, query, geocode, city='', count=20):
        tweets = []

        try:
            fetched_tweets = self.api.search(q=query, count=count, geocode=geocode,
                                              lang="en", tweet_mode="extended", truncated=False)

            for tweet in fetched_tweets:
                parsed_tweet = {}
                parsed_tweet['text'] = tweet.full_text
                parsed_tweet['sentiment'] = self.get_sentiment(tweet.full_text)
                parsed_tweet['polarity'] = self.get_polarity(tweet.full_text)
                parsed_tweet['city'] = city
                # get the coordinate info
                coordinates = geocode.split(",")
                parsed_tweet['lat'] = float(coordinates[0])
                parsed_tweet['long'] = float(coordinates[1])

                if tweet.retweet_count > 0:
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            return tweets

        except tweepy.TweepError as e:
            """print error if there is one"""
            print("Error: " + str(e))

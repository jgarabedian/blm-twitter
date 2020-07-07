import tweepy

import json

with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])

api = tweepy.API(auth)
backup = "43.913723261972855,-72.54272478125,150km"
results = api.search(q='blm', count=20, geocode="39.4143,-77.4105,50km")
print(results)

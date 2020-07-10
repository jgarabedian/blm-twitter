from TwitterClient import TwitterClient
from tweetcard import create_deck
import pandas as pd

api = TwitterClient()

geocode = "38.9072,-77.0369,50km"

tweets = api.get_tweets(query="blm", count=10,
                        geocode=geocode, city='Washington, DC')

df = pd.DataFrame(tweets)

html = create_deck(df)

print(html)
from TwitterClient import TwitterClient
import pandas as pd
import flask
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from components import nav
from components import index
from components import sources
from components.method import method_page
from components.dashboards import create_dashboards
from components.tweetcard import create_deck

import json

with open("locations.json", "r") as location_file:
    locations = json.load(location_file)

api = TwitterClient()
tweets = []
for location in locations:
    geocode = str(location['geocode'])
    city_tweets = api.get_tweets(query='blm', count=20, geocode=geocode, city=location['city'])
    tweets = tweets + city_tweets

# picking positive tweets from tweets
# ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
# percentage of positive tweets
# print("Positive tweets percentage: {} %".format(100 * len(ptweets) / len(tweets)))
# picking negative tweets from tweets
# ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
# percentage of negative tweets
# print("Negative tweets percentage: {} %".format(100 * len(ntweets) / len(tweets)))
# percentage of neutral tweets
# print("Neutral tweets percentage: {} % \
#       ".format(100 * (len(tweets) - (len(ntweets) + len(ptweets))) / len(tweets)))

df = pd.DataFrame(tweets)

server = flask.Flask(__name__)

meta_tags = {
    "name": "BLM Twitter",
    "description": "Analyzing the twitter content across the country around BLM."
}

app = dash.Dash(__name__, server=server, suppress_callback_exceptions=True,
                external_stylesheets=[dbc.themes.SLATE],
                meta_tags=[meta_tags])

app.title = "BLM Twitter"

app.index_string = index.index_string

dash_page = create_dashboards(df)

app.layout = html.Div(children=[
    dcc.Location(id='url', refresh=False),
    html.Div(nav.navbar),
    dbc.Container(
        fluid=True,
        className="main-container",
        children=[
            html.Div(id="page-content")
        ])

])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def update_path(pathname):
    if pathname == '/sources':
        return sources.source_page
    elif pathname == '/':
        return dash_page
    elif pathname == '/method':
        return method_page
    else:
        return dash_page


@app.callback([Output('tweet-deck', 'children'),
               Output('city-name', 'children')],
              [Input('map', 'clickData')])
def filter_tweets(clickData):
    if clickData is None:
        return '', ''
    city = clickData['points'][0]['text']
    new_tweets = create_deck(df, city)
    return new_tweets, city


if __name__ == "__main__":
    app.run_server(debug=True, use_reloader=True)

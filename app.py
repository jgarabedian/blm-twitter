from TwitterClient import TwitterClient
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import pandas as pd
import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from components import nav
from components import index


import json
with open("locations.json", "r") as location_file:
    locations = json.load(location_file)

with open("mapbox_credentials.json", "r") as mapbox:
    token = json.load(mapbox)

mapbox_token = token[0]['token']

api = TwitterClient()
tweets = []
for location in locations:
    geocode = str(location['geocode'])
    city_tweets = api.get_tweets(query='blm', count=20, geocode=geocode, city=location['city'])
    tweets = tweets + city_tweets

# picking positive tweets from tweets
ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
# percentage of positive tweets
print("Positive tweets percentage: {} %".format(100 * len(ptweets) / len(tweets)))
# picking negative tweets from tweets
ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
# percentage of negative tweets
print("Negative tweets percentage: {} %".format(100 * len(ntweets) / len(tweets)))
# percentage of neutral tweets
print("Neutral tweets percentage: {} % \
      ".format(100 * (len(tweets) - (len(ntweets) + len(ptweets))) / len(tweets)))


# print the most positive tweet
df = pd.DataFrame(tweets)
# print('\nShow me a positive tweet\n\n')
# print(df['text'][df['polarity'] == max(df['polarity'])])
# print('\nShow me the most negative tweet\n\n')
# print(df['text'][df['polarity'] == min(df['polarity'])])

df2 = df.groupby(['city']).mean().reset_index()
token = "pk.eyJ1IjoiamdhcmFiZWRpYW45NiIsImEiOiJja2NiOXIwMHoyMzBoMnlvNjlvbDM5YjdpIn0.kDrWnOiNYLSpA0zR_6Gyjw"
fig = px.scatter_mapbox(data_frame=df2, lat="lat", lon="long",
                        color="polarity", color_continuous_scale=px.colors.diverging.Picnic,
                        color_continuous_midpoint=0, zoom=3, text="city")
fig.update_layout(mapbox_style="dark", mapbox_accesstoken=mapbox_token, template="plotly_dark")

avg_sent_fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=df['polarity'].mean(),
    title={"text": "Average Polarity of Tweets"},
    domain = {'x': [0, 1], 'y': [0, 1]},
    gauge={
        "axis": {
            "range": [-1,1]
        },
        "bar": {
            "color": "rgb(91, 192, 222)"
        }
    }
))

avg_sent_fig.layout.template = 'plotly_dark'

server = flask.Flask(__name__)


meta_tags = {
    "name": "BLM Twitter",
    "description": "Analyzing the twitter content across the country around BLM."
}

app = dash.Dash(__name__, server=server,
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[meta_tags])

app.title = "BLM Twitter"

app.index_string = index.index_string

app.layout = html.Div(children=[
    html.Div(nav.navbar),
    dbc.Container(
        fluid=True,
        className="bg-secondary",
        children=[
            html.H5(
                className="text-white pt-2",
                children=[
                    "Analyzing the sentiment of tweets that mention BLM"
                ]
            ),
            dbc.Row(children=[
                dbc.Col(
                    className="mb-2 mt-2",
                    children=[
                        dcc.Graph(figure=fig)
                    ])
            ]),
            dbc.Row(
                children=[
                    dbc.Col(
                        className="mb-2",
                        children=[
                            dcc.Graph(figure=avg_sent_fig)
                        ]
                    )
                ]
            )

    ])

])

if __name__ == "__main__":
    # run the server
    app.run_server(debug=True,use_reloader=True)

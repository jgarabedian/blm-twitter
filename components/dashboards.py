from components.tweetcard import create_deck
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import os

mapbox_token = os.environ.get("MAPBOX_TOKEN")


def create_dashboards(df):
    df2 = df.groupby(['city']).mean().reset_index()

    fig = px.scatter_mapbox(data_frame=df2, lat="lat", lon="long",
                            color="polarity", color_continuous_scale=px.colors.diverging.Picnic,
                            color_continuous_midpoint=0, zoom=3, text="city",
                            title="Tweets by City")
    fig.update_layout(mapbox_style="dark", mapbox_accesstoken=mapbox_token,
                      template="plotly_dark")

    avg_sent_fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=df['polarity'].mean(),
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            "axis": {
                "range": [-1, 1]
            },
            "bar": {
                "color": "rgb(91, 192, 222)"
            }
        }
    ))
    avg_sent_fig.update_layout(title_text="Average Polarity of Tweets")
    avg_sent_fig.layout.template = 'plotly_dark'

    colors = ["rgb(2, 117, 216)", "rgb(247, 247, 247)", "rgb(217, 83, 79)"]

    df3 = df.groupby('sentiment').agg({"text":"nunique"}).reset_index()
    print(df3)

    bar_fig = go.Figure(go.Pie(
        labels=df3['sentiment'],
        values=df3['text'],
        hole=.4,
        marker=dict(colors=colors)
    ))

    bar_fig.update_layout(title_text="Distribution of Sentiment")

    bar_fig.layout.template = 'plotly_dark'

    dash_page = html.Div(
        children=[
            html.H5(
                className="pt-2",
                children=[
                    "Analyzing the sentiment of tweets that mention BLM"
                ]
            ),
            html.P(children='Click on the map to see the tweets we\'re analyzing '),
            dbc.Row(children=[
                dbc.Col(
                    className="mb-2 mt-2",
                    children=[
                        dcc.Graph(figure=fig, id="map")
                    ])
            ]),
            dbc.Row(
                children=[
                    dbc.Col(
                        className="mb-2",
                        lg=4,
                        md=12,
                        sm=12,
                        children=[
                            # html.Div(
                            dcc.Graph(figure=avg_sent_fig,
                                      className="pb-2"),
                            # ),
                            dcc.Graph(figure=bar_fig)
                        ]
                    ),
                    dbc.Col(
                        className="mb-2",
                        lg=8,
                        md=12,
                        sm=12,

                        children=[
                            dbc.Container(
                                fluid=True,
                                children=[
                                    html.H3(
                                        id="city-name"
                                    ),
                                    dbc.ListGroup(
                                        id="tweet-deck",
                                        children=create_deck(df, None),
                                        flush=True

                                    )
                                ]
                            )
                        ]
                    )
                ])

        ])
    return dash_page

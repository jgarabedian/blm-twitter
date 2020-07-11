import dash_html_components as html
import dash_bootstrap_components as dbc

method_page = html.Div(
    children=[
    dbc.Jumbotron([
        html.H1("Welcome", className=" display-3"),
        html.P(
            "This is a site I built to analyze the sentiment of tweets regarding BLM",
            className="lead"
        ),
        html.Hr(),
        html.P([
            "I started by bringing in tweets from various cities that I picked purely out of curiosity. ",
            "From there, I utilized NLP with TextBlob to understand the sentiment of the tweets that were brought in. "
            "Now that I have all the data, we can start visualizing."
        ]),
        html.P([
            "IMPORTANT NOTE: We are analyzing the sentiment of the tweet, but not of the subject matter BLM. ",
            "This is an important clarification, because it is not an indication of the users feelings towards BLM."
        ])
    ],
    className="mt-2")
    ]

)
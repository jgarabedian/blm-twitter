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
            html.Hr(className="bg-secondary"),
            html.P([
                "I started by bringing in tweets from various cities that I picked purely out of curiosity. ",
                "From there, I utilized NLP with TextBlob to understand the sentiment of the tweets that were brought "
                "in. "
                "Now that I have all the data, we can start visualizing."
            ]),
            html.P([
                "IMPORTANT NOTE: We are analyzing the sentiment of the tweet, but not of the subject matter BLM. ",
                "This is an important clarification, because it is not an indication of the users feelings towards BLM."
            ]),
            html.Hr(className="bg-secondary"),
            html.H3(
                children=[
                    'We Support Black Lives Matter #BLM'
                ],
                className="text-uppercase"
            ),
            html.P(dbc.Button("Find a place to donate", color="primary",
                              className="btn-lg", href="http://blmdonate.com/", target="_blank"), className="lead")
        ],
            className="mt-2",
        )
    ]
)

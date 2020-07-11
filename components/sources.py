import dash_html_components as html
import dash_bootstrap_components as dbc


def create_card(title, source, link):
    return dbc.Card(
        children=[
            html.H5(title, className="card-title"),
            dbc.CardLink(source, href=link, target="_blank")
        ],
        body=True)


source_page = html.Div(
    # className='d-flex justify-content-around',
    children=[
        dbc.Row(className="m-4",
                children=[
                    dbc.Col(
                        className="mb-2",
                        children=[create_card("Twitter API", "Twitter", "https://developer.twitter.com/en/docs")],
                        width=12,
                        sm=12,
                        lg=6,
                        xl=4,
                    ),
                    dbc.Col(
                        className="mb-2",
                        children=[
                            create_card("Twitter API Package", "Tweepy", "http://docs.tweepy.org/en/latest/api.html")],
                        width=12,
                        sm=12,
                        lg=6,
                        xl=4,
                    ),
                    dbc.Col(
                        className="mb-2",
                        children=[create_card("Visualizations", "Plotly Dash", "https://plotly.com/dash/")],
                        width=12,
                        sm=12,
                        lg=6,
                        xl=4,
                    ),
                    dbc.Col(
                        className="mb-2",
                        children=[create_card("Natural Language Processing", "TextBlob",
                                              "https://textblob.readthedocs.io/en/dev/")],
                        width=12,
                        sm=12,
                        lg=6,
                        xl=4,

                    )
                ])
    ]
)

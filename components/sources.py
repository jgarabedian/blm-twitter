import dash_html_components as html

source_page = html.Div(
    children=[
        html.H4(
            className="text-white",
            children=[
                'Twitter API',
                html.P(children=[
                    html.Em(children=[
                        html.A(children=['Twitter Developers'],
                               href="https://developer.twitter.com/en/docs",
                               target="_blank")
                    ])
                ])
            ]),
        html.H4(
            className="text-white",
            children=[
                'Twitter Python Package',
                html.P(children=[
                    html.Em(children=[
                        html.A(children=['Tweepy'],
                               href="http://docs.tweepy.org/en/latest/api.html",
                               target="_blank")
                    ])
                ])
            ]),
        html.H4(
            className="text-white",
            children=[
                'Visualizations',
                html.P(children=[
                    html.Em(children=[
                        html.A(children=['Plotly Dash'],
                               href="https://plotly.com/dash/",
                               target="_blank")
                    ])
                ])
            ]),
        html.H4(
            className="text-white",
            children=[
                'Text Processing',
                html.P(children=[
                    html.Em(children=[
                        html.A(children=['TextBlob'],
                               href="https://textblob.readthedocs.io/en/dev/",
                               target="_blank")
                    ])
                ])
            ])
    ]
)

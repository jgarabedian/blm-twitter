import dash_html_components as html

source_page = html.Div(
    className='d-flex justify-content-around',
    children=[
        html.H4(
            className="text-white float-left p-2",
            children=[
                html.U('Twitter API'),
                html.P(children=[
                    html.Em(children=[
                        html.A(children=['Twitter Developers'],
                               className='text-light',
                               href="https://developer.twitter.com/en/docs",
                               target="_blank")
                    ])
                ])
            ]),
        html.H4(
            className="text-white float-left p-2",
            children=[
                html.U('Twitter Python Package'),
                html.P(children=[
                    html.Em(children=[
                        html.A(children=['Tweepy'],
                               className='text-light',
                               href="http://docs.tweepy.org/en/latest/api.html",
                               target="_blank")
                    ])
                ])
            ]),
        html.H4(
            className="text-white float-left p-2",
            children=[
                html.U('Visualizations'),
                html.P(children=[
                    html.Em(children=[
                        html.A(children=['Plotly Dash'],
                               className='text-light',
                               href="https://plotly.com/dash/",
                               target="_blank")
                    ])
                ])
            ]),
        html.H4(
            className="text-white float-left p-2",
            children=[
                html.U('Text Processing'),
                html.P(children=[
                    html.Em(children=[
                        html.A(children=['TextBlob'],
                               className='text-light',
                               href="https://textblob.readthedocs.io/en/dev/",
                               target="_blank")
                    ])
                ])
            ])
    ]
)

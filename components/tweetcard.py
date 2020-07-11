import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd


def create_deck(df: pd.DataFrame, city: str) -> html.Div:
    if city is not None:
        df = df[df['city'] == city]

    list_items = []
    for index, row in df.iterrows():
        if row['sentiment'] == 'positive':
            text_color = "text-danger"
        elif row['sentiment'] == 'neutral':
            text_color = "text-light"
        else:
            text_color = "text-primary"
        tweet = dbc.ListGroupItem(
            children=[
                html.Div(
                    className="tweetcard",
                    children=[
                        html.Div(
                            className="tweetcard__icon",
                            children=[
                                html.Img(
                                    src="/assets/images/Twitter_Logo_Blue.png",
                                    className="tweetcard__icon__logo"
                                )
                            ]
                        ),
                        html.Div(
                            className="tweetcard__content text-white text-wrap",
                            children=[
                                row['text'],
                                html.Div(
                                    children=[
                                        row['city'], html.Div(
                                            className=text_color,
                                            children=[row['sentiment']])
                                    ],
                                    className="tweetcard__content__meta font-italic text-info"
                                ),

                            ]
                        )

                    ]
                )
            ],
            action=True,
            className="bg-dark text-white border border-white text-break text-wrap",
        )
        list_items.append(tweet)

    return list_items

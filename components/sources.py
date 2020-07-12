import dash_html_components as html
import dash_bootstrap_components as dbc

import json
with open("sources.json", "r") as source_file:
    sources = json.load(source_file)


def create_card(title: str, source: str, link: str) -> dbc.Card:
    """
    Create the Card with the appropriate arguments
    :param title: str - title of the card
    :param source: str - source of what we're using
    :param link: str - link to source
    :return: dbc.Card
    """
    return dbc.Card(children=[
            dbc.CardHeader(html.H5(title, className="card-title")),
            dbc.CardBody(dbc.CardLink(source, href=link, target="_blank"))
        ])


def create_col(card: dbc.Card) -> dbc.Col:
    """Pass each card to create a Col element"""
    return dbc.Col(
        className="mb-2",
        children=[card],
        width=12,
        sm=12,
        lg=6,
        xl=4
    )


def create_source_page() -> list:
    """Create elements for children of row"""
    cols = []
    for source in sources:
        card = create_card(source['title'], source['source'], source['href'])
        cols.append(create_col(card))

    return cols


source_page = html.Div(
    children=[
        dbc.Row(className="m-4",
                children=create_source_page())
    ]
)

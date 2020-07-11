import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(
            dbc.NavLink("Sources", href="/sources")
        )
    ],
    brand="BLM Twitter Analysis",
    brand_href="/",
    color="dark",
    fluid=True,
    dark=True,
    className="border-bottom border-light"
)
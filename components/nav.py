import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(
            dbc.NavLink("Sources", href="/sources")
        ),
        dbc.NavItem(
            dbc.NavLink("Method", href="/method")
        )
    ],
    brand="BLM Twitter Analysis",
    brand_href="/",
    color="primary",
    fluid=True,
    dark=True,
    # className="border-bottom border-light"
)
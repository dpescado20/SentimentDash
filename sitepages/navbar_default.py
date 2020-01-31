import dash_bootstrap_components as dbc


def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Login", href="/login")),
        ],
        brand="Sentiment Analysis",
        brand_href="/home",
        sticky="top",
    )

    return navbar

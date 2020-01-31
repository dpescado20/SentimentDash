import dash_bootstrap_components as dbc


def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/home")),
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Social Media",
                children=[
                    dbc.DropdownMenuItem("Twitter"),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("YouTube"),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Facebook"),
                ],
            ),
            dbc.NavItem(dbc.NavLink("API", href="https://sentiment-analyzer-api.herokuapp.com/", external_link=True)),
            dbc.NavItem(dbc.NavLink("Logout", href="/home")),
        ],
        brand="Sentiment Analysis",
        brand_href="/home",
        sticky="top",
    )

    return navbar

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from sitepages.navbar_default import Navbar

nav = Navbar()

body = dbc.Container(
    [
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Jumbotron(
                            [
                                html.H1("Jumbotron", className="display-3"),
                                html.P(
                                    "Use a jumbotron to call attention to "
                                    "featured content or information.",
                                    className="lead",
                                ),
                                html.Hr(className="my-2"),
                                html.P(
                                    "Jumbotrons use utility classes for typography and "
                                    "spacing to suit the larger container."
                                ),
                                html.P(dbc.Button("Learn more", color="primary"), className="lead"),
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)


def Homepage():
    layout = html.Div([
        nav,
        body
    ])

    return layout

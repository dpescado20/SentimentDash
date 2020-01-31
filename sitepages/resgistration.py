import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from sitepages.navbar_default import Navbar

nav = Navbar()
firstname_input = dbc.FormGroup(
    [
        dbc.Label("First Name"),
        dbc.Input(type="text", id="txb-firstname", placeholder="Enter first name")
    ]
)

lastname_input = dbc.FormGroup(
    [
        dbc.Label("Last Name"),
        dbc.Input(type="text", id="txb-lastname", placeholder="Enter last name"),
    ]
)

email_input = dbc.FormGroup(
    [
        dbc.Label("Email", html_for="example-email"),
        dbc.Input(type="email", id="txb-email", placeholder="Enter email"),
    ]
)

password_input = dbc.FormGroup(
    [
        dbc.Label("Password", html_for="example-password"),
        dbc.Input(
            type="password",
            id="txb-password",
            placeholder="Enter password",
        )
    ]
)

signup_button = dbc.Button("Sign Up", color="primary", block=True, href="/login", id="btn-password")

radios_input = dbc.FormGroup(
    [
        dbc.Label("Account Type", html_for="example-radios-row"),
        dbc.RadioItems(
            id="rb-accounttype",
            options=[
                {"label": "Developer", "value": 1},
                {"label": "Non - Developer", "value": 2},
            ]
        )
    ]
)

body = dbc.Container(
    [
        html.Br(),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(),
                dbc.Col(
                    [
                        dbc.Form(
                            [
                                firstname_input,
                                lastname_input,
                                email_input,
                                password_input,
                                radios_input,
                                signup_button
                            ]
                        )
                    ]
                ),
                dbc.Col()
            ]
        )
    ]
)


def Registration():
    layout = html.Div([
        nav,
        body
    ])

    return layout

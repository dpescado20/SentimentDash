import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from sitepages.navbar_default import Navbar

nav = Navbar()
email_input = dbc.FormGroup(
    [
        dbc.Label("Email", html_for="example-email"),
        dbc.Input(type="email", id="txb-email", placeholder="Enter email")
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

submit_button = dbc.Button("Login", color="success", block=True, id="btn-login", href="/nondev")
signup_button = dbc.Button("Sign Up", color="primary", block=True, href="/signup")

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
                                email_input,
                                password_input,
                                submit_button,
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


def LogIn():
    layout = html.Div([
        nav,
        body
    ])

    return layout

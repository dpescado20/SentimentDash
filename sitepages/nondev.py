import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from sitepages.navbar_nondev import Navbar

nav = Navbar()

text_input = dbc.Card(
    [
        dbc.CardHeader("TOPIC", id='txb-header'),
        dbc.CardBody(
            [
                dbc.Form(
                    [
                        dbc.FormGroup(
                            [
                                dbc.Input(type="text", placeholder="Enter topic", id="txb-topic"),
                            ],
                            className="mr-3",
                        ),
                        dbc.Button("Analyze", color="primary", id="btn-topic")
                    ],
                    inline=True,
                )
            ]
        )
    ]
)

twitter_graph = dbc.Card(
    [
        dbc.CardHeader("TWITTER"),
        # dbc.CardHeader("TWITTER", style={'background-color': '#38A1F3', 'color': 'white'}),
        dbc.CardBody(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Label(html.H6(id="lbl-total-tweets"))
                        )
                    ]
                ),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dcc.Graph(id='graph-twitter', style={'height': 300}),
                                dcc.Interval(
                                    id='interval-component',
                                    interval=3 * 1000,  # in milliseconds
                                    n_intervals=0
                                )
                            ]
                        ),
                        dbc.Col(
                            [
                                dbc.Label(html.H6(id='lbl-tweet1')),
                                html.Br(),
                                html.Br(),
                                dbc.Label(html.H6(id='lbl-score'))
                            ]
                        )
                    ]
                )
            ]
        ),
    ]
)

body = dbc.Container(
    [
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        text_input,
                        html.Br(),
                        twitter_graph,
                        html.Br(),
                        html.Br()
                    ]
                )
            ]
        )
    ]
)


def NonDev():
    layout = html.Div([
        nav,
        body
    ])

    return layout

import random

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State
import os
from collections import deque
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

from sitepages.homepage import Homepage
from sitepages.login import LogIn
from sitepages.resgistration import Registration
from sitepages.nondev import NonDev

from sitesocial.ex_twitter import ExtractTweet

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])
server = app.server

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/login':
        return LogIn()
    elif pathname == '/signup':
        return Registration()
    elif pathname == '/nondev':
        return NonDev()
    else:
        return Homepage()


for root, dirs, files in os.walk("sitedata/twitter/score"):
    for file in files:
        os.remove(os.path.join(root, file))

for root, dirs, files in os.walk("sitedata/twitter/tweet"):
    for file in files:
        os.remove(os.path.join(root, file))

# GLOBAL VARIABLES
pos = 1
neg = 1
file_count = 1
score = 0

X = deque(maxlen=50)
X.append(0)
Y = deque(maxlen=50)
Y.append(0)


@app.callback(
    Output('txb-header', 'value'),
    [Input('btn-topic', 'n_clicks')],
    [State('txb-topic', 'value')]
)
def run_twitter(n_clicks, value):
    twitter = ExtractTweet()
    twitter.stop_stream()

    for root, dirs, files in os.walk("sitedata/twitter/score"):
        for file in files:
            os.remove(os.path.join(root, file))

    for root, dirs, files in os.walk("sitedata/twitter/tweet"):
        for file in files:
            os.remove(os.path.join(root, file))

    global file_count
    global pos
    global neg
    global score

    pos = 1
    neg = 1
    file_count = 1
    score = 0

    twitter.extract_tweet(value)
    return 'running'


@app.callback(
    [Output('graph-twitter-pie', 'figure'),
     Output('lbl-total-tweets', 'children'),
     Output('lbl-tweet1', 'children'),
     Output('lbl-score', 'children'),
     Output('graph-twitter-line', 'figure')],
    [Input('interval-component', 'n_intervals')])
def update_twitter_graph_pie(n):
    global file_count
    global pos
    global neg
    global score

    try:
        with open(f"sitedata/twitter/score/{file_count}.txt", "r") as file:
            text = file.read().strip()
            score = float(text)
            if float(text) < 0:
                neg += 1
                sentiment = "Negative Sentiment"
            elif float(text) > 0:
                pos += 1
                sentiment = "Positive Sentiment"
            # file_count += 1

    except EnvironmentError as e:
        print(e)
        sentiment = "Waiting for Tweets..."

    try:
        with open(f"sitedata/twitter/tweet/{file_count}.txt", "r") as xfile:
            tweet = xfile.read()
            file_count += 1

    except EnvironmentError as e:
        print(e)
        tweet = "Fetching Tweets..."

    # Pie Graph
    figure_pie = go.Figure(
        data=[
            go.Pie(
                values=[pos, neg],
                labels=['Positive', 'Negative'],
                hoverinfo='label+percent',
                hole=0.4,
                sort=False
            )
        ],
        layout=go.Layout(
            margin=go.layout.Margin(l=40, r=0, t=40, b=30)
        )
    )

    # Line Graph
    X.append(X[-1] + 1)
    Y.append(score)
    figure_line = dict(
        data=[
            dict(
                x=list(X),
                y=list(Y),
                marker=dict(
                    color='rgb(55, 83, 109)',
                    mode='lines+markers',
                )
            )
        ],
        layout=dict(
            margin=dict(l=40, r=0, t=40, b=30),
            xaxis=dict(
                tickmode='linear',
                tick0=0,
                dtick=1,
                title='Refresh Count (3 Seconds)'
            ),
            yaxis=dict(
                title='Sentiment Score'
            ),
        )
    )
    # figure_line = go.Figure(
    #     data=[
    #         go.Scatter(
    #             x=list(X),
    #             y=list(Y),
    #             name='Scatter',
    #             mode='lines+markers',
    #             opacity=0.7
    #         )
    #     ],
    #     layout=go.Layout(
    #         xaxis=dict(
    #             tickmode='linear',
    #             tick0=0,
    #             dtick=1,
    #             title='Refresh Count (3 Seconds)'
    #         ),
    #         yaxis=dict(
    #             title='Sentiment Score'
    #         ),
    #         margin={'l': 40, 'b': 40, 't': 10, 'r': 10}
    #     )
    # )

    return figure_pie, f"TOTAL TWEETS : {file_count - 1}", f"TWEET : {tweet}", f"SENTIMENT : {sentiment}", figure_line


if __name__ == '__main__':
    app.run_server(threaded=True, dev_tools_ui=False)

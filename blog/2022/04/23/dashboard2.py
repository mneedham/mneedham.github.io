import datetime
from dash import Dash, html, dcc, Input, Output

app = Dash(__name__)
app.layout = html.Div([
    html.Div(children=[
        dcc.Slider(min=0.5, max=5, step=0.5, value=1, id='interval-refresh'), #<1>
    ], style={'width': '20%'}),
    html.Div(id='latest-timestamp', style={"padding": "20px"}),
    dcc.Interval(
            id='interval-component',
            interval=1 * 1000,
            n_intervals=0
    ),
])

@app.callback(
    [Output(component_id='interval-component', component_property='interval')],
    [Input('interval-refresh', 'value')])
def update_refresh_rate(value):
    return [value * 1000] #<2>

@app.callback(
    [Output(component_id='latest-timestamp', component_property='children')],
    [Input('interval-component', 'n_intervals')]
)
def update_timestamp(interval):
    return [html.Span(f"Last updated: {datetime.datetime.now()}")] 

if __name__ == '__main__':
    app.run_server(debug=True)
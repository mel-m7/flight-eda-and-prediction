import dash
import dash_html_components as html
from dash.dependencies import Input, Output
from pages import page1, page2, page3

app = dash.Dash(__name__, suppress_callback_exceptions=True)

# Define main app layout
app.layout = html.Div([
    html.Div([
        html.H1('Indian Flights Price Analysis and Visualization', style={'textAlign': 'center'}),
    ], style={'marginBottom': '30px'}),

    html.Div([
        html.Button('General Statistics', id='btn-general', n_clicks=0,
                    style={'marginRight': '10px', 'backgroundColor': '#4CAF50', 'border': 'none', 'color': 'white',
                           'padding': '15px 32px', 'text-align': 'center', 'text-decoration': 'none',
                           'display': 'inline-block', 'font-size': '16px'}),
        html.Button('Price Depending on Days', id='btn-price-days', n_clicks=0,
                    style={'marginRight': '10px', 'backgroundColor': '#008CBA', 'border': 'none', 'color': 'white',
                           'padding': '15px 32px', 'text-align': 'center', 'text-decoration': 'none',
                           'display': 'inline-block', 'font-size': '16px'}),
        html.Button('Map', id='btn-map', n_clicks=0,
                    style={'backgroundColor': '#f44336', 'border': 'none', 'color': 'white', 'padding': '15px 32px',
                           'text-align': 'center', 'text-decoration': 'none', 'display': 'inline-block',
                           'font-size': '16px'})
    ], style={'textAlign': 'center', 'marginBottom': '30px'}),

    # Placeholder for page content, will be updated based on button clicks
    html.Div(id='page-content')
])


# Callback to update page content based on button clicks
@app.callback(
    Output('page-content', 'children'),
    [Input('btn-general', 'n_clicks'),
     Input('btn-price-days', 'n_clicks'),
     Input('btn-map', 'n_clicks')]
)
def display_page(btn_general, btn_price_days, btn_map):
    ctx = dash.callback_context
    if not ctx.triggered:
        button_id = 'btn-general'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'btn-general':
        return page1.layout
    elif button_id == 'btn-price-days':
        return page2.layout
    elif button_id == 'btn-map':
        return page3.layout


if __name__ == '__main__':
    app.run_server(debug=True)

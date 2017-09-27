# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

df = pd.read_csv('vote.csv', error_bad_lines=False)

print('****************************************')
print(df)
print('****************************************')

colors = {
    'background': '#4e4e4e',
    'text': '#e7ff6e'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Australian Marriage Law Postal Survey',
        style={
            'textAlign': 'center',
            'color': colors['text'],
            'font-family': 'Helvetica'
        }
    ),

    html.Div(children='A Quick Introduction to Dash', style={
        'textAlign': 'center',
        'color': colors['text'],
        'font-family': 'Helvetica'
    }),

    dcc.Graph(
        id='same-sex-vote',
        figure={
            'data': [
                go.Bar(
            x=['Yes', 'No'],
            y=[69, 44]
    	)],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']                    
                }
            }
        }
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)

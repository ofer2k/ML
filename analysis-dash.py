import numpy as np 
import pandas as pd 
import configparser

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output


from utils.data import data_frame_stat

config = configparser.ConfigParser()
config.read('config.ini')

df=data_frame_stat(config)
data_mat0,data_mat1,target = df.target_split()
N=data_mat0.shape[1]




external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(className='grid-container',children=[
    
    html.Div(className='item1',children=[
        html.H1(children='The Data Exploration Tool')
        ,html.H2(children='A data web application exploration tool.')
    ]),

    html.Div(className='item2',children=[
        dcc.Dropdown(
            id='column1',
            options=[ {'label': str(n), 'value': n} for n in range(N) ],
            value=0,
            multi=False
        ),
        dcc.Dropdown(
            id='column2',
            options=[ {'label': str(n), 'value': n} for n in range(N) ],
            value=1,
            multi=False
        )
    ]),

    html.Div(className='item3',children=[
        dcc.Graph(
            id='scatter-graph',
            figure={
                'data': [],
                'layout': {
                    'title': 'Scatter Data Visualization'
                    }
            }
        ),

        dcc.Graph(   
            id='hist-graph',    
            figure={
                'data': [],
                'layout': {
                    'title': 'Histogram Data Visualization'
                }

            }
        ),
    dcc.Graph(   
            id='violin-graph',    
            figure=df.violin_plot()
        )    

    ]),

    html.Div(className='item5',children=[
        dcc.Graph(   
            id='stat0-graph',    
            figure=df.mean_std_plot()
        )
    ])

])


@app.callback([Output('scatter-graph', 'figure'),Output('hist-graph', 'figure')],[Input(component_id='column1', component_property='value'),Input(component_id='column2', component_property='value')])
def update_output_div(v0,v1):
    
    trace0 = go.Scatter(
        x = data_mat0[:,v0],
        y = data_mat0[:,v1],
        mode = 'markers'
    )
    trace1 = go.Scatter(
        x = data_mat1[:,v0],
        y = data_mat1[:,v1],
        mode = 'markers'
    )

    data_scatter = [trace0,trace1]

    data_hist = [go.Histogram(x=data_mat0[:,v0]),go.Histogram(x=data_mat0[:,v1])]

    figure1={
            'data': data_scatter,
            'layout': {
                'title': 'Scatter Data Visualization'
                }
        }    
    figure2={
            'data': data_hist,
            'layout': {
                'title': 'Histogram Data Visualization'
            }

        }
    return figure1,figure2

if __name__ == '__main__':
    app.run_server(debug=True)

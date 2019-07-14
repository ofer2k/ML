import numpy as np 
import pandas as pd 
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

df= pd.read_csv('train.csv')
print(df.head())
N=299
start_i=3
end_i=start_i+N

f0=df['target']==0.0
f1=df['target']==1.0
data0=df[f0]
data1=df[f1]

data_mat0=data0.iloc[:,start_i:end_i].to_numpy()
data_mat1=data1.iloc[:,start_i:end_i].to_numpy()

target=df['target'].to_numpy()
print(data_mat0.shape)
print(data_mat1.shape)





external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Training data exploration'),

    html.Div(children='''
         A data web application exploration tool.
    '''),

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
    ),

    dcc.Graph(
        id='scatter-graph',
        figure={
            'data': [],
            'layout': {
                'title': 'Scatter Data Visualization'
                }
        }),

    dcc.Graph(   
        id='hist-graph',    
        figure={
            'data': [],
            'layout': {
                'title': 'Histogram Data Visualization'
            }

        }
    )
])


@app.callback([Output('scatter-graph', 'figure'),Output('hist-graph', 'figure')],[Input(component_id='column1', component_property='value'),Input(component_id='column2', component_property='value')]
)
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
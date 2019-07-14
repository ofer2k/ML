import numpy as np 
import pandas as pd 
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

df= pd.read_csv('train.csv')
print(df.head())

f0=df['target']==0.0
f1=df['target']==1.0
data0=df[f0]
data1=df[f1]

data_mat0=data0.iloc[:,3:302].to_numpy()
data_mat1=data1.iloc[:,3:302].to_numpy()

target=df['target'].to_numpy()
print(data_mat0.shape)
print(data_mat1.shape)


trace0 = go.Scatter(
    x = data_mat0[:,0],
    y = data_mat0[:,1],
    mode = 'markers'
)
trace1 = go.Scatter(
    x = data_mat1[:,0],
    y = data_mat1[:,1],
    mode = 'markers'
)

data_scatter = [trace0,trace1]
data_hist = [go.Histogram(x=data_mat0[:,0]),go.Histogram(x=data_mat0[:,1])]


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Training data exploration'),

    html.Div(children='''
         A data web application exploration tool.
    '''),

    dcc.Graph(
        id='scatter-graph',
        figure={
            'data': data_scatter,
            'layout': {
                'title': 'Scatter Data Visualization'
                }
        }),

    dcc.Graph(   
        id='hist-graph',    
        figure={
            'data': data_hist,
            'layout': {
                'title': 'Histogram Data Visualization'
            }

        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
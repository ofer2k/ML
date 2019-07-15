import numpy as np 
import pandas as pd 
import plotly.plotly as py
import plotly.graph_objs as go


def mean_std(data):
    m=np.mean(data,axis=0)
    s=np.std(data,axis=0)
    return m,s



def mean_std_plot(data0,data1):
    mean0,std0=mean_std(data0)
    mean1,std1=mean_std(data1)
    n0=mean0.shape[0]
    x0=np.arange(0,n0)
    n1=mean1.shape[0]
    x1=np.arange(0,n1)

    print(f'n0:{n0} n1:{n1}')
    trace1 = go.Bar(
        y=mean0,
        x=x0,
        name='mean0'
    )
    trace2 = go.Bar(
        y=mean1,
        x=x1,
        name='mean1'
    )

    data = [trace1, trace2]
    layout = go.Layout(
        barmode='group'
    )

    fig = go.Figure(data=data, layout=layout)    
    return fig

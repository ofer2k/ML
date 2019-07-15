import numpy as np 
import pandas as pd 
import plotly.plotly as py
import plotly.graph_objs as go


def mean_std(data):
    m=np.mean(data,axis=0)
    s=np.std(data,axis=0)
    return m,s




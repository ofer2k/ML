import numpy as np 
import pandas as pd 

import plotly.plotly as py
import plotly.graph_objs as go

from utils.stat import mean_std


class data_frame_stat():
    def __init__(self,config):
        df= pd.read_csv(config['Data']['file'])

        start_i=int(config['Data']['start_idx'])
        end_i=df.shape[1]
        

        f0=df[config['Target']['name']]==0.0
        f1=df[config['Target']['name']]==1.0
        data0=df[f0]
        data1=df[f1]


        self.data_mat0=data0.iloc[:,start_i:end_i].to_numpy()
        self.data_mat1=data1.iloc[:,start_i:end_i].to_numpy()

        self.target=df[config['Target']['name']].to_numpy()
        #print(data_mat0.shape)
        #print(data_mat1.shape)

    def target_split(self):
        return self.data_mat0,self.data_mat1,self.target

    def mean_std_plot(self):
        mean0,std0=mean_std(self.data_mat0)
        mean1,std1=mean_std(self.data_mat0)
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

    def violin_plot(self):
        data = []
        cc=0
        for d in [self.data_mat0,self.data_mat1]:
            for i in [0,1]:
                trace = {
                        "type": 'violin',
                        "x": str(cc),
                        "y": d[:,i],
                        "name": str(cc),
                        "box": {
                            "visible": True
                        },
                        "meanline": {
                            "visible": True
                        }
                    }
                
                cc += 1
                data.append(trace)

                
        fig = {
            "data": data,
            "layout" : {
                "title": "",
                "yaxis": {
                    "zeroline": False,
                }
            }
        }

        return fig


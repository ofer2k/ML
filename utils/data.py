import numpy as np 
import pandas as pd 
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

    def stat(self):
        mean0,std0=mean_std(self.data_mat0)
        mean1,std1=mean_std(self.data_mat1)        


import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time

data=pd.read_csv('./new_data.csv')
in_flow=np.zeros((3479,32,48),dtype='i')
out_flow=np.zeros((3479,32,48),dtype='i')

a=data.loc[:,['start station id','starttime','end station id','stoptime']]

for i in a.itertuples():
    t=time.strptime(str(i[2]),"%Y-%m-%d %H:%M:%S")
    j=int(i[1])
    k=int(t.tm_mday)
    l=int(t.tm_hour*2+t.tm_min/30)
    out_flow[j][k][l]=out_flow[j][k][l]+1
    t=time.strptime(str(i[4]),"%Y-%m-%d %H:%M:%S")
    j=int(i[3])
    k=int(t.tm_mday)
    l=int(t.tm_hour*2+t.tm_min/30)
    in_flow[j][k][l]=in_flow[j][k][l]+1

with open('inout_flow_data.csv','w') as x:
    o=csv.writer(x)
    o.writerow(['station_id','time','in_flow_count','out_flow_count'])
    for i in range(1,3479):
        for j in range(1,32):
            for k in range(48):
                o.writerow([i,(j-1)*48+k,in_flow[i][j][k],out_flow[i][j][k]])
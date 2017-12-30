import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time

base=6
for i in range(4,8):
    v=str(i)
    data=pd.read_csv('./20170'+v+'-citibike-tripdata.csv')
    in_flow=np.zeros((3479,32,48),dtype='i')
    out_flow=np.zeros((3479,32,48),dtype='i')
    print(v)
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
    with open('0'+v+'_inout_flow_data_2.csv','w') as x:
        o=csv.writer(x)
        m=32 if int(v)%2==1 else 31
        print(m,' ',base)
        o.writerow(['day','station_id','time','in_flow_count','out_flow_count'])
        for i in range(1,3479):
            d=base
            for j in range(1,m):
                for k in range(48):
                    o.writerow([d,i,str(v)+'-'+str((j-1)*48+k),in_flow[i][j][k],out_flow[i][j][k]])
                d=(d+1)%8
                d=1 if d==0 else d
        base=d
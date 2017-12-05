import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import pairwise_distances

data=pd.read_csv('./inout_flow_data.csv')

d=data.loc[data['station_id']==519,:]

print(pairwise_distances([d['in_flow_count'],d['out_flow_count']],metric='euclidean'))

plt.figure(figsize=(15,15))
plt.plot(d['time'],d['in_flow_count'],color='blue',label='in',linewidth=1.0)
plt.plot(d['time'],d['out_flow_count'],color='red',label='out',linewidth=1.0)
a=[]
for i in range(-2,80):
    a.append(i)
for i in range(1,32):
	plt.plot([48*i]*82,a,color='gray',linewidth=0.5)
plt.title('station 519 in/out flow count')
plt.xlabel('time')
plt.ylabel('count')
plt.legend()
plt.show()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import pairwise_distances

data=pd.read_csv('./inout_flow_data.csv')

d=data.loc[data['station_id']==519,:]
plt.figure(figsize=(15,15))
im=np.mean(d['in_flow_count'])
isd=np.std(d['in_flow_count'])
om=np.mean(d['out_flow_count'])
osd=np.std(d['out_flow_count'])

print(pairwise_distances([(d['in_flow_count']-im)/isd,(d['out_flow_count']-om)/osd],metric='euclidean'))

plt.plot(d['time'],(d['in_flow_count']-im)/isd,color='blue',label='in',linewidth=1.0)
plt.plot(d['time'],(d['out_flow_count']-om)/osd,color='red',label='out',linewidth=1.0)
a=[]
for i in range(-1,5):
    a.append(i)
for i in range(1,32):
	plt.plot([48*i]*6,a,color='gray',linewidth=0.5)
plt.title('station 519 in/out flow count')
plt.xlabel('time')
plt.ylabel('count')
plt.legend()
plt.show()


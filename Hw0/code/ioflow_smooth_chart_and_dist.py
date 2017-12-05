import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.nonparametric.smoothers_lowess import lowess
from sklearn.metrics.pairwise import pairwise_distances

data=pd.read_csv('./inout_flow_data.csv')

d=data.loc[data['station_id']==519,:]

inf = lowess(d['in_flow_count'], d['time'], frac=0.007, it=0)
outf = lowess(d['out_flow_count'], d['time'], frac=0.007, it=0)

print(pairwise_distances([inf[:,1],outf[:,1]],metric='euclidean'))

plt.figure(figsize=(15,15))
plt.plot(inf[:,0],inf[:,1],color='blue',label='in',linewidth=1.0)
plt.plot(outf[:,0],outf[:,1],color='red',label='out',linewidth=1.0)
a=[]
for i in range(-10,70):
    a.append(i)
for i in range(1,32):
	plt.plot([48*i]*80,a,color='gray',linewidth=0.5)
plt.title('station 519 in/out flow count')
plt.xlabel('time')
plt.ylabel('count')
plt.legend()
plt.show()

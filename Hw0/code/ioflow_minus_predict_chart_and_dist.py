import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics.pairwise import pairwise_distances

data=pd.read_csv('./inout_flow_data.csv')

reg=linear_model.LinearRegression()
d=data.loc[data['station_id']==519,:]

x=d['time']
i=d['in_flow_count']
o=d['out_flow_count']
x=x.values.reshape([len(x),1])
i=i.values.reshape([len(i),1])
o=o.values.reshape([len(o),1])
reg.fit(x,i)
inp=reg.predict(x)
reg.fit(x,o)
outp=reg.predict(x)
inp=np.reshape(inp,len(inp))
outp=np.reshape(outp,len(outp))
i=np.reshape(i,len(i))
o=np.reshape(o,len(o))
x=np.reshape(x,len(x))

print(pairwise_distances([i-inp,o-outp],metric='euclidean'))

plt.figure(figsize=(15,15))
plt.plot(x,i-inp,color='blue',label='in',linewidth=1.0)
plt.plot(x,o-outp,color='red',label='out',linewidth=1.0)
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


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import time
from sklearn.cluster import AgglomerativeClustering
import numpy as np

data=pd.read_csv('./station_data.csv')
data1=data.iloc[:,[2,3]]
data2=pd.read_csv('./inout_flow_data.csv')
d=[]
ids=list(data.loc[:,'end station id'])

for i in ids:
	now=data2.loc[(data2['station_id']==i)&(data2['time']>=0)&(data2['time']<336),'in_flow_count']
	d.append(now)
	# now=data2.loc[(data2['station_id']==i)&(data2['time']>=0)&(data2['time']<336),'out_flow_count']
	# if(now.value_counts()[0]!=336):
	# 	ids.append('out'+str(i))
	# 	d.append(now)
k=3
ac=AgglomerativeClustering(n_clusters=k).fit(d)

for idx in range(0,k):
	lat=[]
	lon=[]
	for index,value in data1.iterrows():
		if(ac.labels_[index]==idx):
			lat.append(value['end station latitude'])
			lon.append(value['end station longitude'])
	plt.scatter(lat,lon,s=5,label=idx)

plt.title('cluster with AgglomerativeClustering k='+str(k))
plt.xlabel('latitude')
plt.ylabel('longitude')
plt.legend()
plt.show()
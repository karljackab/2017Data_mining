import pandas as pd
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv('./inout_flow_data.csv')
d=[]

for i in range(1,3479):
	now=data.loc[(data['station_id']==i)&(data['time']>=0)&(data['time']<336),'in_flow_count']
	if(now.value_counts()[0]!=336):
		d.append(now)
	now=data.loc[(data['station_id']==i)&(data['time']>=0)&(data['time']<336),'out_flow_count']
	if(now.value_counts()[0]!=336):
		d.append(now)

k=7
time=np.arange(336)
col=['blue','red','#76FF03','orange','#FFEB3B','#29B6F6','#ff8a80','gold','#607D8B','#BA68C8','#18FFFF','#6D7480']
ac=AgglomerativeClustering(n_clusters=k).fit(d)
plt.figure(figsize=(7,6),dpi=100)
for idx in range(0,k):
	pnow=plt.subplot(k,1,idx+1)
	for i in range(len(d)):
		if(ac.labels_[i]==idx):
			pnow.plot(time,d[i],color=col[idx],linewidth=1)
			pnow.xlabel('time')
			pnow.ylabel('count')
			pnow.yticks([0,25,50])
plt.show()



# d1=data.loc[data['time']<336,['time','in_flow_count']]
# d1.columns.values[1]='count'
# d2=data.loc[data['time']<336,['time','out_flow_count']]
# d2.columns.values[1]='count'
# data=pd.concat([d1,d2]).drop_duplicates()
# data=data.set_index(np.arange(data.count()[0]))
# k=7
# time=np.arange(336)
# col=['blue','red','#76FF03','orange','#FFEB3B','#29B6F6','#ff8a80','gold','#607D8B','#BA68C8','#18FFFF','#6D7480']
# ac=AgglomerativeClustering(n_clusters=k).fit(d)
# print(ac.labels_)
# plt.figure(figsize=(7,6),dpi=100)
# for idx in range(0,k): #plot different color for each cluster
# 	x=[]
# 	y=[]
# 	for i in range(len(d)):
# 		if(ac.labels_[i]==idx):
# 			x.append(time)
# 			y.append(d[i])
# 	plt.scatter(x,y,s=5,color=col[idx],label=idx)
# plt.title('cluster with Agglomerative Clustering k='+str(k))
# plt.xlabel('time')
# plt.ylabel('count')
# plt.legend()
# plt.show()
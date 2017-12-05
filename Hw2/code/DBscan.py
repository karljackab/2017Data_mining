import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
import time

t_start=time.time()

data=pd.read_csv('./station_data.csv')
data=data.iloc[:,[2,3]]
dbscan=DBSCAN(eps=30/6371,min_samples=5,metric='haversine').fit(data)
col=['blue','red','#76FF03','orange','#FFEB3B','#29B6F6','#ff8a80','gold','#607D8B','#BA68C8','#18FFFF','#6D7480']
plt.figure(figsize=(7,6),dpi=100)
k=len(set(dbscan.labels_))-(1 if -1 in dbscan.labels_ else 0)
print(k)
for idx in range(-1,k):
	lat=[]
	lon=[]
	for index,value in data.iterrows():
		if(dbscan.labels_[index]==idx):
			lat.append(value['end station latitude'])
			lon.append(value['end station longitude'])
	if idx==-1:
		plt.scatter(lat,lon,s=5,color='black',label='outlier')
	else:
		plt.scatter(lat,lon,s=5,color=col[idx],label=idx)

print('It cost '+str(round(time.time()-t_start,6))+' s.')
plt.title('cluster with dbscan cluster_number='+str(k))
plt.xlabel('latitude')
plt.ylabel('longitude')
plt.legend()
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import time

t_start=time.time()

k=12 #set clustering number value
data=pd.read_csv('./station_data.csv')
data=data.iloc[:,[2,3]] #extract latitude and longitude
kmeans=KMeans(n_clusters=k,n_init=15).fit(data)
col=['blue','red','#76FF03','orange','#FFEB3B','#29B6F6','#ff8a80','gold','#607D8B','#BA68C8','#18FFFF','#6D7480']
plt.figure(figsize=(7,6),dpi=100)
for idx in range(0,k): #plot different color for each cluster
	lat=[]
	lon=[]
	for index,value in data.iterrows():
		if(kmeans.labels_[index]==idx):
			lat.append(value['end station latitude'])
			lon.append(value['end station longitude'])
	plt.scatter(lat,lon,s=5,color=col[idx],label=idx)

print('It cost '+str(round(time.time()-t_start,6))+' s.')
plt.title('cluster with KMeans k='+str(k))
plt.xlabel('latitude')
plt.ylabel('longitude')
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

cluster_range=range(1,20)
data=pd.read_csv('./station_data.csv')
data=data.iloc[:,[2,3]]
errors=[]

plt.figure(figsize=(7,5))
for k in cluster_range: #record sum of squared distances to their closest center for each k values 
	kmeans=KMeans(n_clusters=k,n_init=15).fit(data)
	errors.append(kmeans.inertia_)
plt.plot(cluster_range,errors,marker='o')
plt.xticks(np.linspace(0,20,21))
plt.title('elbow method')
plt.xlabel('cluster number')
plt.ylabel('sum of squared distances')
plt.show()

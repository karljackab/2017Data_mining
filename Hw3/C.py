from sklearn.ensemble import GradientBoostingRegressor
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

def extract(data,x,y):
	Max=len(data)-48*14
	for i in range(0,Max,48): #for everyday as the first day
		for j in range(48):	#to extract every period of a day
			d=[]
			for k in range(14): #for the 14 days of a set of data
				d.append(data[i+j+48*k][1]*10000+data[i+j+48*k][0])
			x[j].append(d)
			y[j].append(data[i+j+48*14][1])

def plot(y_t,y_pred):
    t=[]
    pred=[]
    for i in range(len(y_t[0])):
        for j in range(len(y)):
            t.append(y_t[j][i])
            pred.append(y_pred[j][i])
    plt.figure(figsize=(12,10))
    plt.xlabel('time')
    plt.ylabel('out_flow_count')
    plt.plot(np.arange(len(t)),t,label='original')
    plt.plot(np.arange(len(pred)),pred,label='predict')
    plt.legend()
    plt.show()

def gradient(x,y,x_t,y_t,y_pred):
	for i in range(48):
		classifier=GradientBoostingRegressor()
		classifier.fit(x[i],y[i])
		y_pred[i]=classifier.predict(x_t[i])
	return mean_squared_error(y_t,y_pred)

data=pd.read_csv('test_data.csv')
x=pd.read_csv('train_data_2.csv').loc[:,['day','out_flow_count']]
x_t=data.loc[:,['day','out_flow_count']]
X=(np.array(x)).astype(int).tolist()
X_t=(np.array(x_t)).astype(int).tolist()

x=[]
y=[]
x_t=[]
y_t=[]
y_pred=[]
for i in range(48): #initialize
	x.append([])
	y.append([])
	x_t.append([])
	y_t.append([])
	y_pred.append([])
extract(X,x,y)
extract(X_t,x_t,y_t)
tstart=time.time()

print(gradient(x,y,x_t,y_t,y_pred))
print('It cost '+str(round(time.time()-tstart,5))+' s.')
plot(y_t,y_pred)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import PassiveAggressiveClassifier
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

def extract(data,x,y):
    Max=len(data)-48*14
    for i in range(0,Max,48):#for everyday as the first day
        for j in range(48):#to extract every period of a day
            d=[]
            for k in range(14):#for the 14 days of a set of data
                d.append(data[i+j+48*k])
            x[j].append(d)
            y[j].append(data[i+j+48*14])

def plot(y_t,y_pred):
    t=[]
    pred=[]
    for i in range(len(y_t[0])):
        for j in range(len(y)):
            t.append(y_t[j][i])
            pred.append(y_pred[j][i])
    plt.figure(figsize=(15,13))
    plt.xlabel('time')
    plt.ylabel('out_flow_count')
    plt.scatter(np.arange(len(t)),t,s=13,c='red',label='original')
    plt.scatter(np.arange(len(pred)),pred,s=13,c='white',label='predict')
    plt.legend()
    plt.show()

def K_Near(x,y,x_t,y_t,y_pred,n):
	score=0
	t=0
	for i in range(48):
		classifier=KNeighborsClassifier(n_neighbors=n)
		classifier.fit(x[i],y[i])
		y_pred[i]=classifier.predict(x_t[i])
		print(x_t[i])
		print(y_pred[i])
		score+=classifier.score(x_t[i],y_t[i])
		t+=1
	return score/t

def Gaussian_NB(x,y,x_t,y_t,y_pred):
	score=0
	t=0
	for i in range(48):
		classifier=GaussianNB()
		classifier.fit(x[i],y[i])
		y_pred[i]=classifier.predict(x_t[i])
		score+=classifier.score(x_t[i],y_t[i])
		t+=1
	return score/t

def RandomForest(x,y,x_t,y_t,y_pred):
	score=0
	t=0
	for i in range(48):
		classifier=RandomForestClassifier()
		classifier.fit(x[i],y[i])
		y_pred[i]=classifier.predict(x_t[i])
		score+=classifier.score(x_t[i],y_t[i])
		t+=1
	return score/t

def svc(x,y,x_t,y_t,y_pred):
	score=0
	t=0
	for i in range(48):
		classifier=SVC()
		try:
			classifier.fit(np.array(x[i]),np.array(y[i]))
			y_pred[i]=classifier.predict(x_t[i])
			score+=classifier.score(x_t[i],y_t[i])
			t+=1
		except:
			print('error in '+str(i))
			y_pred[i]=np.zeros(17)
			continue
	return score/t

def pac(x,y,x_t,y_t,y_pred):
	score=0
	t=0
	for i in range(48):
		classifier=PassiveAggressiveClassifier(max_iter=len(x[i]))
		try:
			classifier.fit(np.array(x[i]),np.array(y[i]))
			y_pred[i]=classifier.predict(x_t[i])
			score+=classifier.score(x_t[i],y_t[i])
			t+=1
		except:
			print('error in '+str(i))
			y_pred[i]=np.zeros(17)
			continue
	return score/t

def print_confusion(y_t,y_pred):
	y=np.array(y_t)
	p=np.array(y_pred)
	count=len(y)
	total=y.max()
	total=np.maximum(total,p.max())
	print("Original:",end='')
	print(list(y_t))
	print("Predict :",end='')
	print(list(y_pred))
	print(end='\t')
	for i in range(total+1):
		print(i,end='\t\t')
	print()
	for i in range(total+1):
		print(i,end='\t')
		for j in range(total+1):
			c=0
			for k in range(len(y)):
				if(y[k]==i and p[k]==j):
					c+=1
			print(str(c)+'/'+str(count)+'('+str(round(c/count,3))+')',end='\t')
		print()


disc=5
data=pd.read_csv('07_inout_flow_data.csv')
x=pd.read_csv('train_data.csv').loc[:,'out_flow_count']
x_t=data.loc[data['station_id']==519,'out_flow_count']
X=(np.array(x)/disc).astype(int).tolist()
X_t=(np.array(x_t)/disc).astype(int).tolist()

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

# a=[]
# for i in range(1,100):
#     a.append(RandomForest(x,y,x_t,y_t,y_pred,i))
# plt.plot(np.linspace(1,100,59),a)
# plt.show()

tstart=time.time()

# print(K_Near(x,y,x_t,y_t,y_pred,1))
# print(RandomForest(x,y,x_t,y_t,y_pred))
# print(svc(x,y,x_t,y_t,y_pred))
# print(pac(x,y,x_t,y_t,y_pred))

print('It cost '+str(round(time.time()-tstart,5))+' s.')


plot(y_t,y_pred)
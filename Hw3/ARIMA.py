from statsmodels.tsa.arima_model import ARIMA
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

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

def parser(x):
    base=int(x[2:])
    day=int(base/48)+1
    h=int(base%48/2)
    m=base%2*30
    result='2017-'+x[0:2]+str(day)+'-'+str(h)+'-'+str(m)
    return pd.to_datetime(result,format='%Y-%m-%d-%H-%M')

x_t=pd.read_csv('test_data.csv',parse_dates=[2],date_parser=parser).loc[:,['out_flow_count']]
x=pd.read_csv('train_data_2.csv',parse_dates=[2],date_parser=parser).loc[:,['out_flow_count']]
x_t[['out_flow_count']]=x_t[['out_flow_count']].astype(float)
x[['out_flow_count']]=x[['out_flow_count']].astype(float)
train=x.values
test=x_t.values
history=[x for x in train]
for i in range(672):
    history.append(test[i])
test=test[672:]
prediction=list()
tstart=time.time()
print(len(test))
for t in range(len(test)):
    model=ARIMA(history,order=(5,1,0))
    model_fit=model.fit(disp=0)
    output=model_fit.forecast()
    yhat=output[0]
    prediction.append(yhat)
    history.append(test[t])
print(mean_squared_error(test,prediction))
print('It cost '+str(round(time.time()-tstart,5))+' s.')
plt.figure(figsize=(15,13))
plt.xlabel('time')
plt.ylabel('out_flow_count')
plt.plot(test,label='original')
plt.plot(prediction,label='predict')
plt.legend()
plt.show()
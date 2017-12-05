import pandas as pd
import random as rd

data=pd.read_csv('./201707-citibike-tripdata.csv')
for index,i in data.iterrows():
    if(data.loc[index,'gender']==0):
        if(data.loc[index,'usertype']=='Customer'):
            r=rd.randint(1,47580)
            if(r<=30085):
                data.loc[index,'gender']=1
            else:
                data.loc[index,'gender']=2
        if(data.loc[index,'usertype']=='Subscriber'):
            r=rd.randint(1,1452827)
            if(r<=1069299):
                data.loc[index,'gender']=1
            else:
                data.loc[index,'gender']=2
data.to_csv('./new_data.csv')
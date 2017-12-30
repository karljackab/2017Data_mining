import pandas as pd

data=pd.DataFrame()
for i in range(3,7):
	v=str(i)
	a=pd.read_csv('0'+v+'_inout_flow_data_2.csv')
	a=a.loc[a['station_id']==519,:]
	data=pd.concat([data,a])
data.to_csv('train_data_2.csv',index=False)

data=pd.read_csv('07_inout_flow_data_2.csv')
data=data.loc[data['station_id']==519,:]
data.to_csv('test_data.csv',index=False)
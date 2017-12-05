import pandas as pd
from orangecontrib.associate.fpgrowth import * 
from mlxtend.preprocessing import OnehotTransactions

data=pd.read_csv('./inout_flow_data.csv')
data=data.loc[(data['station_id']==519) & ((data['in_flow_count']!=0) | (data['out_flow_count']!=0)),['in_flow_count','out_flow_count']]

lst=[]
for value in data.itertuples():
	if(value[1]<10):
		a=value[1]/2+1
	else:
		a=6+(value[1]-10)/10
	if(value[2]<10):
		b=value[2]/2+1
	else:
		b=6+(value[2]-10)/10
	lst.append([int(a),int(b)*-1])

itemsets = frequent_itemsets(lst,0.05)
a=list(itemsets)
for i in a:
	if(len(i[0])>1):
		print(i[0],' '+str(round(i[1]/len(lst),6)))
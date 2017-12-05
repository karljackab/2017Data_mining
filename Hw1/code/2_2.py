import pandas as pd
from orangecontrib.associate.fpgrowth import * 
from mlxtend.preprocessing import OnehotTransactions

data=pd.read_csv('./station_data.csv')
data=data.loc[:,['end station latitude','end station longitude']]

lst=[]
for value in data.itertuples():
	lst.append([(int((value[1]-40.655399322509766)/0.02)),int(((value[2]+73.89659881591797)/0.02))])

itemsets = frequent_itemsets(lst,0.05)
a=list(itemsets)
for i in a:
	if(len(i[0])>1):
		print(i[0],' '+str(i[1])+' '+str(round(i[1]/634,6)))
import pandas as pd
from orangecontrib.associate.fpgrowth import * 
from mlxtend.preprocessing import OnehotTransactions

data=pd.read_csv('./new_data.csv')
data=data.loc[:,['start station id','end station id','gender']]
lst=[]
for value in data.itertuples():
	lst.append([int(value[1]),-1*int(value[2]),int(value[3])])	

itemsets = frequent_itemsets(lst,0.004)
a=dict(itemsets)
rule=list(association_rules(a,0.8))
print('= = = = =')
for i in rule:
	if(len(i[0])==1):
		print(i[0],i[1],i[2],str(round(i[2]/len(lst),7)),round(i[3],7))
print('= = = = =')

itemsets = frequent_itemsets(lst,0.00015)
a=dict(itemsets)
rule=list(association_rules(a,0.8))

for i in rule:
	if(len(i[0])>1):
		print(i[0],i[1],i[2],str(round(i[2]/len(lst),7)),round(i[3],7))
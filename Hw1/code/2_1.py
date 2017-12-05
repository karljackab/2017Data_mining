import pandas as pd
from mlxtend.preprocessing import OnehotTransactions
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

data=pd.read_csv('./station_data.csv')
data=data.loc[:,['end station latitude','end station longitude']]

lst=[]
for value in data.itertuples():
	lst.append([(int((value[1]-40.655399322509766)/0.001)),int(((value[2]+73.89659881591797)/0.001))])

oht=OnehotTransactions()
oht_ary=oht.fit(lst).transform(lst)
df=pd.DataFrame(oht_ary,columns=oht.columns_)
frequent_itemsets=apriori(df,min_support=0.002,use_colnames=True)

for i in frequent_itemsets.itertuples():
	if(len(i[2])>1):
		print(str(i[1])+' '+str(i[2]))

# rules=association_rules(frequent_itemsets, metric="confidence", min_threshold=0.4)
# print(rules)
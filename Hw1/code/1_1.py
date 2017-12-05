import pandas as pd
from mlxtend.preprocessing import OnehotTransactions
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

data=pd.read_csv('./inout_flow_data.csv')
data=data.loc[(data['station_id']==519) & ((data['in_flow_count']!=0) | (data['out_flow_count']!=0)),['in_flow_count','out_flow_count']]

lst=[]
for value in data.itertuples():
	lst.append(['i'+str(int(value[1]/5)),'o'+str(int(value[2]/5))])	

oht=OnehotTransactions()
oht_ary=oht.fit(lst).transform(lst)
df=pd.DataFrame(oht_ary,columns=oht.columns_)
frequent_itemsets=apriori(df,min_support=0.03,use_colnames=True)
print(frequent_itemsets)
rules=association_rules(frequent_itemsets, metric="confidence", min_threshold=0.4)
print(rules)
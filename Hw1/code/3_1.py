import pandas as pd
from mlxtend.preprocessing import OnehotTransactions
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

data=pd.read_csv('./new_data.csv')
data=data.loc[:,['start station id','end station id','gender']]

lst=[]
for value in data.itertuples():
	lst.append([int(value[1]),int(value[2]),int(value[3])])	

oht=OnehotTransactions()
oht_ary=oht.fit(lst).transform(lst)
df=pd.DataFrame(oht_ary,columns=oht.columns_)
frequent_itemsets=apriori(df,min_support=0.03,use_colnames=True)
print(frequent_itemsets)
# rules=association_rules(frequent_itemsets, metric="confidence", min_threshold=0.4)
# print(rules)
import pandas as pd
import numpy as np
from geopy.distance import great_circle,vincenty

data=pd.read_csv('./new_data.csv')

name={
'start station id':'id',
'start station latitude':'latitude',
'start station longitude':'longitude'}
s=data.loc[:,['start station id','start station latitude','start station longitude']]
s=s.rename(columns=name)
name={
'end station id':'id',
'end station latitude':'latitude',
'end station longitude':'longitude'}
s2=data.loc[:,['end station id','end station latitude','end station longitude']]
s2=s2.rename(columns=name)
s=s.append(s2).drop_duplicates('id').sort_values('id')

suv=0
sug=0
for i in s.itertuples():
	for j in s.itertuples():
		if(j[1]<=i[1]):
			continue
		suv=suv+vincenty((i[2],i[3]),(j[2],j[3])).meters
		sug=sug+great_circle((i[2],i[3]),(j[2],j[3])).meters
print('average of vincenty: '+str(suv/634/633*2))
print('average of great_circle: '+str(sug/634/633*2))
import pandas as pd

l=[]
for i in range(4,8):
	v=str(i)
	print(v)
	data=pd.read_csv('20170'+v+'-citibike-tripdata.csv')
	a=data.loc[:,['end station id','end station name','end station latitude','end station longitude']]
	b=data.loc[:,['start station id','start station name','start station latitude','start station longitude']]
	b.columns=['end station id','end station name','end station latitude','end station longitude']
	a=a.append(b).drop_duplicates('end station id')
	l.append(a)

data=pd.read_csv('201703-citibike-tripdata.csv')
a=data.loc[:,['End Station ID','End Station Name','End Station Latitude','End Station Longitude']]
b=data.loc[:,['Start Station ID','Start Station Name','Start Station Latitude','Start Station Longitude']]
b.columns=['End Station ID','End Station Name','End Station Latitude','End Station Longitude']
out=a.append(b).drop_duplicates('End Station ID')
out.columns=['end station id','end station name','end station latitude','end station longitude']

for i in range(0,len(l)):
	out=out.append(l[i]).drop_duplicates('end station id')

out=out.drop_duplicates('end station id').sort_values('end station id')
out.to_csv('station_data.csv',index=False)
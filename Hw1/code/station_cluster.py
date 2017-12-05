import pandas as pd

data=pd.read_csv('./new_data.csv')


out=data.loc[:,['end station id','end station name','end station latitude','end station longitude']]
out=out.drop_duplicates('end station id').sort_values('end station id')
out.to_csv('station_data.csv',index=False);
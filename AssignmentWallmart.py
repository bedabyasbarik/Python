#how many days close was less than 60 dollar?
import pandas as pd
df=pd.read_csv(r'walmart_stock.csv')
df[df['Close']<60]['Date'].count()

#max and min of volume  column
print(df['Volume'].min())
df['Volume'].max()

#what is the max high per year?
cd=df['Date']
#cd.iloc[1].split('-')[0]
print(cd.size)
for i in range(df['Date'].size):
     df['Date'].loc[i]=df['Date'].loc[i].split('-')[0]
c=df[['Date','High']].groupby('Date').max()



df=pd.read_csv(r'walmart_stock.csv')
for i in range(df['Date'].size):
     df['Date'].loc[i]=df['Date'].loc[i].split('-')[1]
d=df[['Date','Close']].groupby('Date').mean()
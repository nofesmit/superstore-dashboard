import pandas as pd
import datetime as dt

# data readed and saved
df = pd.read_csv('original_data/data.csv')

#Order date corrected with 2 years minus
df['Order Date'] = pd.DatetimeIndex(df['Order Date'],dayfirst=True) - pd.DateOffset(years=2)

#Incorrect order date dropped
#df = df.drop(['Order Date'], axis=1)

#Year column created
df['year'] = pd.DatetimeIndex(df['Order Date']).year

#Days to ship colunm created
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True)
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['days to ship'] = (df['Ship Date'] - df['Order Date']).dt.days
df['month_year'] = df['Order Date'].dt.to_period('m')

#Row ID set as index
df.set_index('Row ID', inplace=True)

#NA rows dropped (11 rows)
#df = df.dropna()

#Rename Sub-Category
df.rename(columns={'Sub-Category': 'subcategory'}, inplace=True)

#Clean data saved to further usage
df.to_csv('clean_data.csv', index=False)
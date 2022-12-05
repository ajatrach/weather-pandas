import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#data = {'animals':  ['cat', 'dog', 'bird','snail'],
#        'not animals': ['table', 'computer', 'ketchup','pumpkin'],
#        }
#dataframe= pd.DataFrame(data)
#print(dataframe)

#a =[1,2,3]
#print(a[0:50]) 
                                              
df = pd.read_csv('weather.csv')  #convert temp to int is dtype={'Temp (F)': int}
df = df.drop(df.columns[6], axis=1)  #remove the last column
df['Temp (F)'] = pd.to_numeric(df['Temp (F)'], errors='coerce') #converts to float, add .astype('Int64') to make int instead
df['RH (%)'] = pd.to_numeric(df['RH (%)'], errors='coerce')
df['Precip (in)'] = pd.to_numeric(df['Precip (in)'], errors='coerce')

#print(df.isnull()) returns table of bool , true if value is Nan
print("nulls before")
print(df['Temp (F)'].isnull().sum())  #print number of nulls   -isnan instead of isnull
        #print(df.isnull().sum()) prints number of nulls in each column
        #print(df.isnull().sum().sum()) prints total num of nulls
df.dropna(axis = 0) #drops rows that have null values (axis=1 to drop columns)
        #df['Temp (F)'].fillna(value=0) #replace nans with value
        #df['Temp (F)'].fillna(axis=0, method='ffill', inplace=True) # replace nans with values in prev row
        #df['Temp (F)'].fillna(value=df['Temp (F)'].mean(), inplace=True) #replace nans with the mean of the column
        #avg of previous and next readings or previous and next days- find min and max of interval and fill
        #precip. assume 0

print(df.info()) #object types and more 

print(df[0:50]) #[["Date","Time"]]
#       print(df.columns[2].mean())
print(df.describe()) #includes mean max and min
print(df[["Temp (F)",'RH (%)','Wind Spd (mph)','Precip (in)']].apply(np.mean)) #specify operations on select columns

#combining date and time
# combine them as strings
new_df = pd.to_datetime(df.Date.astype(str) + ' ' +df.Time.astype(str))
# add column to dataframe
df.insert(2, 'Date+Time', new_df)
print(df)
plt.plot(df["Date+Time"],df["Temp (F)"])
plt.show

#plotting attempt
#plt.close("all")
ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
ts = ts.cumsum()
ts.plot()
plt.show()
#single date time 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

cols_to_use = ["Date","Time","Temp (F)","RH (%)","Wind Spd (mph)","Precip (in)"]
df = pd.read_csv('weather.csv', 
parse_dates=[['Date', 'Time']], 
usecols= cols_to_use,
na_values=['m','M'])  
    #parse_dates combines date and time
    #usecols specifies which col (we are ignoring the last one)
    #na_values allows the data to not be read as chars



df.fillna(method='ffill', inplace=True)  #replace nans with the prev value -do avg

#print(df.to_markdown()) #print the whole table
print(df.info()) #using this to find out name of date time column

df.set_index('Date_Time',inplace=True)
print(df)
#setting index makes this not work :P
#plt.plot(df["Date_Time"],df["Temp (F)"])


#create figure and plotspace
fig, ax = plt.subplots(figsize=(10, 10))

ax.plot(df.index.values,
           df['Temp (F)'],
           color='red')

ax.set(xlabel='Date', ylabel='Temp (F)',
       title='Temp over time')

plt.xticks(rotation=50)  #rotating x axis labels



plt.show()

#hourly granularity to daily  daily max, daily min, daily avg over time
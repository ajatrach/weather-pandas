import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

cols_to_use = ["Date","Time","Temp (F)","RH (%)","Wind Spd (mph)","Precip (in)"]
df = pd.read_csv('weather.csv', 
parse_dates=[['Date', 'Time']], 
usecols= cols_to_use,
na_values=['m','M'])  
    #parse_dates combines date and time
    #usecols specifies which col (we are ignoring the last one)
    #na_values allows the data to not be read as chars



df.fillna(method='ffill', inplace=True)  #replace nans with the prev value -do avg

#make the index date time
df.set_index('Date_Time',inplace=True)

#resample to daily granularity
df_daily=df.resample('D').mean()
df_max=df.resample('D').max()
df_min=df.resample('D').min()

#create figure and plotspace
fig, ax = plt.subplots(figsize=(10, 10))

#plot mean, max, min
ax.plot(df_daily.index.values,
           df_daily['Temp (F)'],
           color='purple', 
           label='mean')

ax.plot(df_max.index.values,
           df_max['Temp (F)'],
           color='red',
           label='max')

ax.plot(df_min.index.values,
           df_min['Temp (F)'],
           color='blue',
           label='min')

#label the graph           
ax.set(xlabel='Date', ylabel='Temp (F)',
       title='Temp over time')

#add a legend
ax.legend()

#rotating x axis labels
ax.tick_params(axis='x', labelrotation = 45)

#-------daily smaller range----
fig, ax3 = plt.subplots(figsize=(10, 10))

ax3.plot(df_daily.index.values,
           df_daily['Temp (F)'],
           color='purple', 
           label='mean')

ax3.plot(df_max.index.values,
           df_max['Temp (F)'],
           color='red',
           label='max')

ax3.plot(df_min.index.values,
           df_min['Temp (F)'],
           color='blue',
           label='min')

ax3.set(xlabel='Date', ylabel='Temp (F)',
       title='Temp over time 2')

ax3.set_xlim([datetime.date(2022,2,1),datetime.date(2022,2,28)])

ax3.legend()

ax3.tick_params(axis='x', labelrotation = 45)


#------- monthly---------------
df_monthly=df.resample('M').mean()
df_maxm=df.resample('M').max()
df_minm=df.resample('M').min()

fig, ax1 = plt.subplots(figsize=(10, 10))

ax1.plot(df_monthly.index.values,
           df_monthly['Temp (F)'],
           color='purple', 
           label='mean')

ax1.plot(df_maxm.index.values,
           df_maxm['Temp (F)'],
           color='red',
           label='max')

ax1.plot(df_minm.index.values,
           df_minm['Temp (F)'],
           color='blue',
           label='min')

ax1.set(xlabel='Date', ylabel='Temp (F)',
       title='Temp over time monthly')

ax1.legend()

ax1.tick_params(axis='x', labelrotation = 45)


plt.show()


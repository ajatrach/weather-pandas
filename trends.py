import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
from statsmodels.tsa.seasonal import seasonal_decompose

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

#do trends before smoothing (doesn't work after smoothing)
#plot decomposition , do period= when using multiplicative
result_mean=seasonal_decompose(df_daily['Temp (F)'], model='additive')
result_max=seasonal_decompose(df_max['Temp (F)'], model='additive')
result_min=seasonal_decompose(df_min['Temp (F)'], model='additive')

#moving average smoothing, subset of 4 days
df_daily=df_daily.rolling(window=4).mean()
df_max=df_max.rolling(window=4).max()
df_min=df_min.rolling(window=4).min()


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

#Seasonality: describes the periodic signal in your time series.
#Trend: describes whether the time series is decreasing, constant, 
#  or increasing over time.
#Noise: describes what remains behind the separation of seasonality 
#  and trend from the time series. In other words, it’s the 
#  variability in the data that cannot be explained by the model.

#plot trends with pandas
result_mean.plot()

#plot trends and observed with matplotlib
fig, decom = plt.subplots(figsize=(10,10))
#TRENDS
decom.plot(result_mean.trend.index, 
            result_mean.trend.values,
            color='thistle',
            label= 'mean trend')

decom.plot(result_max.trend.index, 
            result_max.trend.values,
            color='mistyrose',
            label= 'max trend')

decom.plot(result_min.trend.index, 
            result_min.trend.values,
            color='powderblue',
            label= 'min trend')
#OBSERVED
decom.plot(df_daily.index.values,
           df_daily['Temp (F)'],
           color='purple', 
           label='mean')

decom.plot(df_max.index.values,
           df_max['Temp (F)'],
           color='red',
           label='max')

decom.plot(df_min.index.values,
           df_min['Temp (F)'],
           color='blue',
           label='min')

decom.set(xlabel='Date', ylabel='Temp (F)',
       title='Temp over time (trends)')
decom.legend()
decom.tick_params(axis='x', labelrotation = 45)
decom.plot()

#seeing trend per day
meantrend = result_mean.trend
print(meantrend.to_string())
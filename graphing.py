import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

cols_to_use = ["Date","Time","Temp (F)","RH (%)","Wind Spd (mph)","Precip (in)"]
df = pd.read_csv('weather.csv', parse_dates=[['Date', 'Time']], usecols= cols_to_use)  
    #parse_dates combines date and time
    #usecols specifies which col (we are ignoring the last one)

#convert objects to float (add .astype('Int64') to make int instead)
df['Temp (F)'] = pd.to_numeric(df['Temp (F)'], errors='coerce') 
df['RH (%)'] = pd.to_numeric(df['RH (%)'], errors='coerce')
df['Precip (in)'] = pd.to_numeric(df['Precip (in)'], errors='coerce')

df.fillna(method='ffill', inplace=True)  #replace nans with the prev value

#print(df.to_markdown()) #print the whole table
#print(df.info()) using this to find out name of date time column


plt.plot(df["Date_Time"],df["Temp (F)"])
plt.xticks(rotation=50)  #rotating x axis labels

#df.plot(x='Date_Time', y='Precip (in)',kind="bar")
#precip bar chart attempt

plt.show
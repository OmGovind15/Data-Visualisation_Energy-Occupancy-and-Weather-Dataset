import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

file_path = "C:\\Users\\91878\\Downloads\\weather_comparison\\weather_comparison\\IIITD_and_airport_data.csv"
df = pd.read_csv(file_path)
df['Unnamed: 0'] = pd.to_datetime(df['Unnamed: 0'], format='%d-%m-%Y %H:%M')
df['Unnamed: 0'] = pd.to_datetime(df['Unnamed: 0'])
start_date = pd.to_datetime('2018-03-01')
end_date = pd.to_datetime('2018-03-16')
filtered_df = df[(df['Unnamed: 0'] >= start_date) & (df['Unnamed: 0'] <= end_date)]

plt.figure(figsize=(10, 6))
plt.plot(filtered_df['Unnamed: 0'], filtered_df['IIITD_Humidity'], marker='o', linestyle='-', color='b', label='IIITD Humidity', markersize=3)
plt.plot(filtered_df['Unnamed: 0'], filtered_df['Airport_Humidity'], marker='o', linestyle='-', color='r', label='Airport Humidity', markersize=3)
plt.title('Humidity Comparison from 1 March to 15 March 2018')
plt.xlabel('Timestamp')
plt.ylabel('Humidity (%RH)')

date_formatter = DateFormatter('%d-%b')
plt.gca().xaxis.set_major_locator(plt.matplotlib.dates.DayLocator(interval=2))
plt.gca().xaxis.set_major_formatter(date_formatter)
plt.xticks(rotation=45)
plt.yticks([25,50,75])
plt.legend()
plt.tight_layout()
plt.show()

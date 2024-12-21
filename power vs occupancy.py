import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, AutoDateLocator

power_csv_file_path = "C:\\Users\\91878\\Downloads\\energy_dataset\\energy_dataset\\acad_build_mains.csv"
power_df = pd.read_csv(power_csv_file_path)
power_df['timestamp'] = pd.to_datetime(power_df['timestamp'], unit='s')

start_date_power = pd.to_datetime('2017-04-01')
end_date_power = pd.to_datetime('2017-04-06')  
filtered_power_df = power_df[(power_df['timestamp'] >= start_date_power) & (power_df['timestamp'] <= end_date_power)]

occupancy_csv_file_path = "C:\\Users\\91878\\Downloads\\IIITD_occupancy_dataset\\IIITD_occupancy_dataset\\ACB.csv"
occupancy_df = pd.read_csv(occupancy_csv_file_path)
occupancy_df['timestamp'] = pd.to_datetime(occupancy_df['timestamp'], unit='s')

start_date_occupancy = pd.to_datetime('2017-04-01')
end_date_occupancy = pd.to_datetime('2017-04-06')  
filtered_occupancy_df = occupancy_df[(occupancy_df['timestamp'] >= start_date_occupancy) & (occupancy_df['timestamp'] <= end_date_occupancy)]

power_window_size = 15  
occupancy_window_size = 2 

filtered_power_df['power_smooth'] = filtered_power_df['power'].rolling(window=power_window_size).mean()
filtered_occupancy_df['occupancy_smooth'] = filtered_occupancy_df['occupancy_count'].rolling(window=occupancy_window_size).mean()
filtered_power_df['power_smooth_kw'] = filtered_power_df['power_smooth'] / 1000

fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(filtered_power_df['timestamp'], filtered_power_df['power_smooth_kw'], linestyle='-', color='red', label='Power', alpha=0.7)
ax1.set_xlabel('Timestamp')
ax1.set_ylabel('Power (Smoothed) [KW]', color='red')
ax1.tick_params('y', colors='red')
ax1.set_yticks([0, 20, 40, 60])  
ax2 = ax1.twinx()
ax2.plot(filtered_occupancy_df['timestamp'], filtered_occupancy_df['occupancy_smooth'], marker='o', linestyle='-', color='blue', markersize=3, label='Occupancy', alpha=0.7)
ax2.set_ylabel('Occupancy Count (Smoothed)', color='blue')
ax2.tick_params('y', colors='blue')
ax2.set_yticks([0, 200, 400, 600])  
date_format = DateFormatter('%Y-%m-%d %H:%M:%S')
ax1.xaxis.set_major_formatter(date_format)
ax1.xaxis.set_major_locator(AutoDateLocator())
plt.title('Smoothed Power and Occupancy from 1-Apr-2017 to 5-Apr-2017')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

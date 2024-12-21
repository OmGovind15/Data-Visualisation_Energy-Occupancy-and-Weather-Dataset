import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\91878\Downloads\energy_dataset\energy_dataset\girls_hostel_mains.csv"
df = pd.read_csv(file_path)

df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s', utc=True)
df['timestamp'] = df['timestamp'].dt.tz_convert('Asia/Kolkata')
january_2017_data = df[(df['timestamp'].dt.month == 1) & (df['timestamp'].dt.year == 2017)].copy()
august_2016_data = df[(df['timestamp'].dt.month == 8) & (df['timestamp'].dt.year == 2016)].copy()

january_2017_data['power_kw'] = january_2017_data['power'] / 1000.0
august_2016_data['power_kw'] = august_2016_data['power'] / 1000.0
january_2017_data['hour'] = january_2017_data['timestamp'].dt.hour
august_2016_data['hour'] = august_2016_data['timestamp'].dt.hour
average_power_by_hour_january = january_2017_data.groupby('hour')['power_kw'].mean()
average_power_by_hour_august = august_2016_data.groupby('hour')['power_kw'].mean()

plt.figure(figsize=(12, 6))
plt.plot(average_power_by_hour_january.index, average_power_by_hour_january.values, marker='o', linestyle='-', label='January 2017')
plt.plot(average_power_by_hour_august.index, average_power_by_hour_august.values, marker='o', linestyle='-', label='August 2016')
plt.xlabel('Hour of the Day (Asia/Kolkata Timezone)')
plt.ylabel('Average Power Consumption (kW)')
plt.title('Girls hostel main - Average Power Consumption by Hour')
plt.legend()
plt.show()
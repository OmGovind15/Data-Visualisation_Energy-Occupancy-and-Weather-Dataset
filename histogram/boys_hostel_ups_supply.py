import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = r"C:\Users\91878\Downloads\energy_dataset\energy_dataset\boys_hostel_ups.csv"
df = pd.read_csv(file_path)
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s', utc=True)
df['timestamp'] = df['timestamp'].dt.tz_convert('Asia/Kolkata')
selected_data = df[(df['timestamp'] >= '2013-08-01') & (df['timestamp'] <= '2017-12-31')].copy()
selected_data['power_kw'] = selected_data['power'] / 1000.0

bin_edges = np.arange(int(selected_data['power_kw'].min()) - 0.5, int(selected_data['power_kw'].max()) + 1.5, 1)
plt.figure(figsize=(12, 6))
plt.hist(selected_data['power_kw'], bins=bin_edges, edgecolor='black')
plt.xticks(np.arange(0, 50, 5))
plt.yticks([50000,100000,150000,200000])
plt.xlim(0, 40)
plt.ylim(0, 200000)  
plt.xlabel('Power Consumption (kW)')
plt.ylabel('Frequency')
plt.title('Histogram of Power Consumption (August 2013 to December 2017, Bin Width = 1 kW)')
plt.show()

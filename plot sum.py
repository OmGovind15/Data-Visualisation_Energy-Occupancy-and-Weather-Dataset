import pandas as pd
import matplotlib.pyplot as plt

# Load the combined transformer power CSV file
csv_file_path = "C:\\Users\\91878\\combined_transformer_power.csv"
df = pd.read_csv(csv_file_path)

# Convert 'timestamp' to datetime format (assuming it's in Unix timestamp format)
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')

# Convert power to kWh by multiplying by 3.6 (conversion factor from watts to kWh)
df['power_kwh'] = df['power'] * 3.6  # assuming power is given in watts

# Extract month and year to create a new column 'month_year'
df['month_year'] = df['timestamp'].dt.to_period('M')

# Group by 'month_year' and sum the power values for each group
monthly_power_sum_kwh = df.groupby('month_year')['power_kwh'].sum()

# Plot the histogram
plt.figure(figsize=(10, 6))
monthly_power_sum_kwh.plot(kind='bar', color='blue')
plt.title('Monthly Power Consumption (Nov-2013 to Dec-2017)')
plt.xlabel('Month-Year')
plt.ylabel('Power (KWH)')
plt.xticks(rotation=45, ha='right')
plt.show()


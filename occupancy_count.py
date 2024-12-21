import pandas as pd
import matplotlib.pyplot as plt

occupancy_csv_paths = [
    ("C:\\Users\\91878\\Downloads\\IIITD_occupancy_dataset\\IIITD_occupancy_dataset\\ACB.csv", "Academic Building"),
    ("C:\\Users\\91878\\Downloads\\IIITD_occupancy_dataset\\IIITD_occupancy_dataset\\BH.csv", "Boys hostel"),
    ("C:\\Users\\91878\\Downloads\\IIITD_occupancy_dataset\\IIITD_occupancy_dataset\\GH.csv", "Girls hostel"),
    ("C:\\Users\\91878\\Downloads\\IIITD_occupancy_dataset\\IIITD_occupancy_dataset\\DB.csv", "Dining hall"),
    ("C:\\Users\\91878\\Downloads\\IIITD_occupancy_dataset\\IIITD_occupancy_dataset\\LB.csv", "Library"),
    ("C:\\Users\\91878\\Downloads\\IIITD_occupancy_dataset\\IIITD_occupancy_dataset\\LCB.csv", "lecture hall complex"),
    ("C:\\Users\\91878\\Downloads\\IIITD_occupancy_dataset\\IIITD_occupancy_dataset\\SRB.csv", "facilities building"),
    ]

fig, axs = plt.subplots(len(occupancy_csv_paths), 1, figsize=(10, 8), sharex=True)
start_date = pd.to_datetime('2017-09-03')
end_date = pd.to_datetime('2017-09-10')

for i, (csv_file_path, label) in enumerate(occupancy_csv_paths):
    df = pd.read_csv(csv_file_path)

    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    filtered_df = df[(df['timestamp'] >= start_date) & (df['timestamp'] <= end_date)]

    axs[i].plot(filtered_df['timestamp'], filtered_df['occupancy_count'], color=f'C{i}', label=label)

    if i == len(occupancy_csv_paths) // 2:
        axs[i].set_yticks([0, int(filtered_df['occupancy_count'].max())], minor=False)
        axs[i].set_ylabel('Occupancy Count')
    
    axs[i].set_title(f'{label}')

plt.xlabel('Timestamp')
plt.suptitle('Occupancy Count from 3-Sep-2017 to 10-Sep-2017')
plt.tight_layout()
plt.show()


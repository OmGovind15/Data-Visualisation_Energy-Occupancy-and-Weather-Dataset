import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

file_paths = [
    "C:\\Users\\91878\\Downloads\\energy_dataset\\energy_dataset\\transformer_1.csv",
    "C:\\Users\\91878\\Downloads\\energy_dataset\\energy_dataset\\transformer_2.csv",
    "C:\\Users\\91878\\Downloads\\energy_dataset\\energy_dataset\\transformer_3.csv"
]
grouped_dfs=[]
dfs = [pd.read_csv(file_path) for file_path in file_paths]
for i in range(3):
 dfs[i]['timestamp']=pd.to_datetime(dfs[i]['timestamp'], unit='s')
 dfs[i]['year_month']=dfs[i]['timestamp'].dt.to_period('M')
 grouped_df=dfs[i].groupby('year_month').agg({'power':'sum','timestamp':'count'}).reset_index()
 grouped_df['average power']=grouped_df['power']/grouped_df['timestamp']
 print(grouped_df)
 
 grouped_dfs.append(grouped_df)
merged_df = pd.concat(grouped_dfs, ignore_index=True)
final_result = merged_df.groupby('year_month')['average power'].mean().reset_index()
final_result['average power']=final_result['average power']*0.06
final_result['year_month'] = pd.to_datetime(final_result['year_month'].astype(str), format='%Y-%m')
final_result['year_month_str'] = final_result['year_month'].dt.strftime('%Y-%m')
if not final_result['year_month'].isin(['2015-10']).any():
     october_2015_data = pd.DataFrame({'year_month': ['2015-10'], 'average power': [0]})
     final_result = pd.concat([final_result, october_2015_data], ignore_index=True)
final_result['year_month'] = final_result['year_month'].astype(str)

final_result=final_result.sort_values('year_month')
final_result['year_month_str'] = final_result['year_month_str'].fillna('2015-10')
#print(final_result)
plt.bar(final_result['year_month_str'].astype(str), final_result['average power'])

plt.xlabel('Year-Month')
plt.ylabel('Average energy')
plt.title('Average energy Distribution Over Year-Month')
plt.xticks(rotation=45, ha='right',rotation_mode='anchor')
#plt.show()

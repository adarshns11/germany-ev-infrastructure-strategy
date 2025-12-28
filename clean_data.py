import pandas as pd
import os

file_name = 'germany_ev_data.xlsx'

try:
    df_raw = pd.read_excel(file_name)
    print(" Original file loaded successfully.")
except Exception as e:
    print(f" Error loading file: {e}")
    exit()

df_clean = df_raw.iloc[:, [1, 7, 6, 5, 4]].copy()

df_clean.columns = ['Operator', 'Date', 'Power_kW', 'Plugs', 'Type']

df_clean['Date'] = pd.to_datetime(df_clean['Date'], errors='coerce')

df_clean['Year'] = df_clean['Date'].dt.year

df_clean['Power_kW'] = pd.to_numeric(df_clean['Power_kW'], errors='coerce')

df_clean = df_clean.dropna(subset=['Year', 'Power_kW'])

output_name = 'Germany_EV_Strategy_Final.xlsx'
df_clean.to_excel(output_name, index=False)

print("\n--- STRATEGY DATA WRANGLING COMPLETE ---")
print(f"New file created: {output_name}")
print("\nFirst 5 rows of your cleaned data:")
print(df_clean.head())
print("\nTotal chargers processed:", len(df_clean))
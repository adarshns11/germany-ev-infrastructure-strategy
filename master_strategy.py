import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


plt.close('all')


df = pd.read_excel('Germany_EV_Strategy_Final.xlsx')



df = df[(df['Year'] >= 2017) & (df['Year'] <= 2024)].copy()

df['MW'] = (df['Power_kW'] * df['Plugs']) / 1000


yearly = df.groupby('Year').agg({'Plugs': 'sum', 'MW': 'sum'}).reset_index()


X = yearly['Year'].values.reshape(-1, 1)
model_plugs = LinearRegression().fit(X, yearly['Plugs'])
model_mw = LinearRegression().fit(X, yearly['MW'])

pred_2027_plugs = model_plugs.predict([[2027]])[0]
pred_2027_mw = model_mw.predict([[2027]])[0]


print("\n" + "="*50)
print("     FINAL GERMANY EV STRATEGY REPORT")
print("="*50)
print(f"Projected New Plugs (2027): {pred_2027_plugs:,.0f}")
print(f"Projected New MW (2027):    {pred_2027_mw:,.0f} MW")
print("-" * 50)
print("Years Analyzed: 2017 - 2024")
print("="*50)


fig, ax1 = plt.subplots(figsize=(12,6))
ax2 = ax1.twinx()


ax1.bar(yearly['Year'], yearly['Plugs'], color='#3498db', alpha=0.6, label='Annual New Plugs')

ax2.plot(yearly['Year'], yearly['MW'], color='#e74c3c', marker='o', linewidth=3, label='Annual New MW')

# AXIS FIXES
ax1.set_xticks(yearly['Year']) 
ax1.set_xlim(2016.5, 2024.5)    

ax1.set_ylabel('Number of Plugs', fontsize=12)
ax2.set_ylabel('Total Capacity (MW)', fontsize=12)
plt.title('The Modern EV Era: Growth in Units vs. Power (2017-2024)')

plt.savefig('final_strategy_chart_2024.png')
print("\nSuccess! Final chart saved as 'final_strategy_chart_2024.png'")
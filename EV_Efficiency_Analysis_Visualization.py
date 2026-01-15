import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

#File paths
raw_csv = 'C:\\Users\\ramda\\PycharmProjects\\PythonProject\\EV_Efficiency_Analysis\\data\\raw\\electric_vehicles_spec_2025.csv'
clean_csv = 'C:\\Users\\ramda\\PycharmProjects\\PythonProject\\EV_Efficiency_Analysis\\data\\processed\\electric_vehicles_spec_2025_cleaned.csv'

# Read dataset
df = pd.read_csv(raw_csv)
print(f"Raw Data Shape: {df.shape}")
df.info()

#step 1 -----------------------------------> Cleaning Data

# Fill missing values
df.fillna({
    'number_of_cells': '-1',
    'model': 'Unknown',
    'torque_nm': '-1',
    'fast_charging_power_kw_dc': '-1',
    'fast_charge_port': 'Unknown',
    'towing_capacity_kg': '-1'
}, inplace=True)

# Cleaning  cargo_volume_l and converting banana box to liter
df['cargo_volume_l_Temp'] = df['cargo_volume_l'].astype(str)
df['cargo_volume_l_Num'] = df['cargo_volume_l_Temp'].str.extract(r'(\d+\.?\d*)').astype(float)
df['cargo_volume_l'] = df['cargo_volume_l_Num'].apply(lambda x: x*24 if x < 100 else x)
df.fillna({'cargo_volume_l': '-1'}, inplace=True)
df.drop(columns=['cargo_volume_l_Temp', 'cargo_volume_l_Num'], inplace=True)

# here Saving cleaned Excel to processed folder
os.makedirs(os.path.dirname(clean_csv), exist_ok=True)
df.to_csv(clean_csv, index=False)
print(f"Cleaned CSV saved at: {clean_csv}")

#part 2 -----------------------------------> Analyze the trade-off between efficiency (Wh/km) and performance metrics

#Acceleration (0-100 km/h time)
#op speed (km/h)**
#Torque (Nm)
#Randomly choosing only 25 to get more cleaner look

# chart 1 : Acceleration vs Efficiency
sample_df = df.sample(n=25, random_state=42)  # Randomly pick 25 rows (fixed seed for reproducibility)
plt.figure(figsize=(10, 5))
sns.scatterplot(data=sample_df, x='acceleration_0_100_s', y='efficiency_wh_per_km', hue='brand',s=100)
plt.title('EV Efficiency vs Acceleration')
plt.xlabel('Acceleration (0-100 km/h, seconds)')
plt.ylabel('Efficiency (Wh/km)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
# Faster acceleration = lower seconds, so invert x-axis
#invert x-axis ---> 15 -> 10 -> 5 -> 0
plt.gca().invert_xaxis()
#It makes charts look like ggplot (clean, colorful, grid-style)
plt.style.use('ggplot')
plt.tight_layout()
plt.savefig("C:\\Users\\ramda\\PycharmProjects\\PythonProject\\EV_Efficiency_Analysis\\output\\EV_Efficiency_vs_Acceleration.png")
# Converting the column to numeric, coercing errors to NaN (for example, if some values are non-numeric)
#df['fast_charging_power_kw_dc'] = pd.to_numeric(df['fast_charging_power_kw_dc'], errors='coerce')

#droping rows where conversion failed (NaN values)
#df_clean = df.dropna(subset=['fast_charging_power_kw_dc'])

#Now you can safely get top 25 chargers
#df_sample = df_clean.sample(n=25, random_state=42)

#reducing dataset size to 25 best chargers for clarity
#top_chargers = df_clean.nlargest(25, 'fast_charging_power_kw_dc')

# chart 2 : Fast charging power vs Range
plt.figure(figsize=(10, 5))
sns.scatterplot(data=sample_df, x='fast_charging_power_kw_dc', y='range_km', hue='brand', s=100)
plt.title('Fast Charging Power vs EV Range')
plt.xlabel('Fast Charging Power (kW)')
plt.ylabel('Range (km)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.style.use('ggplot')
plt.tight_layout()
plt.savefig("C:\\Users\\ramda\\PycharmProjects\\PythonProject\\EV_Efficiency_Analysis\\output\\Fast_Charging_Power_vs_EV_Range.png")

# chart 3: Fast charging power vs Efficiency
plt.figure(figsize=(10, 5))
sns.scatterplot(data=sample_df, x='fast_charging_power_kw_dc', y='efficiency_wh_per_km', hue='brand', s=100)
plt.title('Fast Charging Power vs EV Efficiency')
plt.xlabel('Fast Charging Power (kW)')
plt.ylabel('Efficiency (Wh/km)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.style.use('ggplot')
plt.tight_layout()
plt.savefig("C:\\Users\\ramda\\PycharmProjects\\PythonProject\\EV_Efficiency_Analysis\\output\\Fast_Charging_Power_vs_EV_Efficiency.png")

#Part3 -------------------------------------> Printing Charts

plt.show()
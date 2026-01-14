import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

#step 1 -----------------> Cleaning Data

#File paths
raw_csv = 'C:\\Users\\ramda\\PycharmProjects\\PythonProject\\EV_Efficiency_Analysis\\data\\raw\\electric_vehicles_spec_2025.csv'
clean_csv = 'C:\\Users\\ramda\\PycharmProjects\\PythonProject\\EV_Efficiency_Analysis\\data\\processed\\electric_vehicles_spec_2025_cleaned.csv'

# Read dataset
df = pd.read_csv(raw_csv)
print(f"Raw Data Shape: {df.shape}")
df.info()
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

# here Saving cleaned Excel to proccesses folder
os.makedirs(os.path.dirname(clean_csv), exist_ok=True)
df.to_csv(clean_csv, index=False)
print(f"Cleaned CSV saved at: {clean_csv}")



#part 2 -------------------> grouping and binning efficiency col for better visualization
#binning efficiency_wh_per_km col

bins = [0, 100, 200, 300, 400]
labels = ['Very Efficient', 'Efficient', 'Average', 'Inefficient']
df['efficiency_wh_per_km_Binned'] = pd.cut(df['efficiency_wh_per_km'], bins=bins, labels=labels)
df['efficiency_wh_per_km_Binned'] = ( df['efficiency_wh_per_km_Binned'].cat.remove_unused_categories())

# Filtering brands removing unnecessary one's and keeping only top EU brands
top_eu_brands = ['Audi', 'BMW', 'Mercedes-Benz', 'Volkswagen'
    , 'Porsche','Volvo', 'Renault', 'Peugeot', 'Skoda']
#Filtering brands removing unnecessary one's and keeping only top brands in world
top_global_brands = [
    'Tesla', 'Toyota', 'Hyundai', 'Kia',
    'Volkswagen', 'BMW', 'Mercedes-Benz', 'Audi', 'Volvo'
]

# part3 --------------------------> Grouping function
def group_by_efficiency(df, brands):
    # First filter by brands
    filtered = df[df['brand'].isin(brands)].copy()

    # Group and count
    grouped = (
        filtered
        .groupby(['efficiency_wh_per_km_Binned', 'brand'], observed=False)
        .size()
        .reset_index(name='count')
    )
    return grouped


#calling group_by_efficiency and passing  parameters

# grouping car as per brand
world_grouped = group_by_efficiency(df, top_global_brands)
eu_grouped = group_by_efficiency(df, top_eu_brands)

#part 4 ------------------------------------> Printing grouped bar chart


#It makes charts look like ggplot (clean, colorful, grid-style)
plt.style.use('ggplot')
fig, axes = plt.subplots(1, 2, figsize=(18, 6))
#creating custom pallet for efficiency
custom_palette = {
    'Very Efficient': '#2E8B57',   # Sea green
    'Efficient': '#66C2A5',        # Light green
    'Average': '#FF8C00',           # Orange
    'Inefficient': '#FF6347'       # Tomato red
}
#world_grouped bar chart
sns.barplot(
    data=world_grouped,
    x='brand',
    y='count',
    hue='efficiency_wh_per_km_Binned',
    palette = custom_palette,
    ax=axes[0]
)

axes[0].set_title('World Top EV Brands – Efficiency')
axes[0].set_xlabel('EV Car Brands')
axes[0].set_ylabel('Efficiency (Wh/km)')
axes[0].tick_params(axis='x', rotation=20)

#eu_grouped bar chart
sns.barplot(
    data=eu_grouped,
    x='brand',
    y='count',
    palette = custom_palette,
    hue = 'efficiency_wh_per_km_Binned',
    ax=axes[1]
)
axes[1].set_title('European Top EV Brands – Efficiency')
axes[1].set_xlabel('EV Car Brands')
axes[1].set_ylabel('Efficiency (Wh/km)')
axes[1].tick_params(axis='x', rotation=20)
# adjusting labes so they don't get cut of and fit in frame
plt.tight_layout()
#saving it to local folder
output_file_path = 'C:\\Users\\ramda\\PycharmProjects\\PythonProject\\EV_Efficiency_Analysis\\output\\electric_vehicles_efficiency_charts.png'
os.makedirs(os.path.dirname(output_file_path),exist_ok=True) # make a new folder if it not there
plt.savefig(output_file_path, dpi= 300) #300 high resolution
print(f"Charts saved at: {output_file_path}")

plt.show()
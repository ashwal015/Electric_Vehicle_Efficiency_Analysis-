Electric_Vehicle_Efficiency_Analysis

Brief Summary
Analyzing the trade-off between EV efficiency, performance, and charging characteristics using Python.
________________________________________
Overview
This project explores how different electric vehicle (EV) models balance efficiency (Wh/km), range, acceleration, and fast-charging capabilities.
Visualizations help compare brands and identify patterns between performance and energy usage.
________________________________________
Key Visualizations
•	Acceleration vs Efficiency – How fast EVs compare in terms of energy consumption.
•	Fast Charging Power vs Range – Relation between charging speed and driving range.
•	Fast Charging Power vs Efficiency – Trade-offs between efficiency and fast-charging capabilities.
PNG charts are generated and saved in outputs/
________________________________________
Problem Statement
How do different EV models trade-off between performance, efficiency, and fast charging capabilities?
Can we identify patterns or trends that help consumers or engineers optimize EV usage?
________________________________________
Dataset
•	Source: Kaggle – EV Efficiency 2025
•	Key fields: brand, model, top_speed_kmh, battery_capacity_kWh, efficiency_wh_per_km, range_km, acceleration_0_100_s, fast_charging_power_kw_dc, etc.
________________________________________
Tools and Technology
•	IDE: PyCharm
•	Languages: Python 3.x
•	Libraries: pandas, matplotlib.pyplot, seaborn, os
________________________________________
Method
1.	Load and clean dataset (pandas)
2.	Filter and sample data for clarity
3.	Visualize relationships between key metrics using scatterplots and boxplots
4.	Save all plots automatically with clear filenames for later use
5.	Analyze trends to extract insights
________________________________________
Key Insights
•	EVs with larger batteries tend to have higher range but are not always the most efficient.
•	Fast charging power varies significantly by brand, and higher charging speeds don’t always correlate with efficiency.
•	Acceleration and efficiency often show a trade-off — faster EVs consume more energy per km.
More detailed insights can be inferred from generated charts.
________________________________________
Dashboard / Model / Output
All visualizations are saved as PNG files in the outputs/folder:
•	EV_Efficiency_vs_Acceleration.png
•	Fast_Charging_Power_vs_EV_Efficiency.png
•	Fast_Charging_Power_vs_EV_Range.png
________________________________________
How to Run Project and Project Structure
Project Structure
```
EV_Efficiency_Analysis/
│
├── EV_Efficiency_Analysis_Visualization.py      # Main Python script
├── outputs/                                     # Saved PNG visualizations
├── README.md
└── data/
    ├── raw/
    │   └── electric_vehicles_spec_2025.csv     # Original dataset
    └── processed/
        └── electric_vehicles_spec_2025_cleaned.csv  # Cleaned dataset
```
Steps to Run
1.	Clone the repo:
git clone https://github.com/ashwal015/Electric_Vehicle_Efficiency_Analysis-
2.	Open in PyCharm or any Python IDE
3.	Install dependencies:
pip install pandas matplotlib seaborn
4.	Run the script:
python EV_Efficiency_Analysis_Visualization.py
5.	View generated plots in outputs/
________________________________________
Results and Conclusion
•	EV efficiency is strongly influenced by battery size and acceleration performance.
•	Fast charging capabilities show brand-specific variations; consumers may prioritize either range, speed, or charging time depending on their needs.
•	Visualizations clearly highlight trade-offs between efficiency and performance, aiding in data-driven decision-making.
________________________________________
Future Work
•	Add interactive dashboard using Plotly or Streamlit
•	Include more datasets with real-world driving data
•	Predict efficiency based on battery, motor, and drivetrain parameters using simple regression models
•	Explore lifecycle analysis including charging habits and battery degradation

# Germany EV Infrastructure: 2027 Strategic Forecast 

Summary
This project analyzes the historical deployment of EV charging infrastructure in Germany from 2017 to 2024 to forecast the market landscape for 2027. By leveraging a 100k-row dataset from the Federal Network Agency (BNetzA), this model identifies a massive "Market Mix Shift" toward High-Power Charging (HPC).

Findings
* **2027 Market Forecast:** ~54,890 new plugs and **4.1 Gigawatts (GW)** of new annual power capacity.
* **Segment Evolution:** Ultra-Fast (HPC) charging (>150kW) is growing faster than standard AC charging, becoming the primary driver of installed Megawatts.
* **Strategic Implication:** Quantitative proof of a massive market pull for **Silicon Carbide (SiC)** power modules, essential for the industry's transition to 800V vehicle architectures.

Tech Stack
* ** Language:** Python 3.x
* * Data Engineering:** Pandas, NumPy
* ** Machine Learning:** Scikit-Learn (Linear Regression)
* ** Visualization:** Matplotlib (Dual-Axis & Stacked Bar Charts)

 1. Visualizations
Market Scale (Units vs. Power Capacity)
The gap between "Plug Count" and "Total Megawatts" is widening, indicating higher power density per installation.

2. The Mix Shift (Segmented Growth)
HPC (Ultra-Fast) has moved from a niche category to the dominant share of new capacity.

 Repository Structure
- clean_data.py: Script for data cleaning and pre-processing.
- master_strategy.py: Main modeling and visualization script.
- Germany_EV_Strategy_Final.xlsx: The processed dataset used for analysis.

 to Run
1. Clone the repository: git clone https://github.com/yourusername/repo-name.git`
2. Install dependencies: pip install pandas scikit-learn matplotlib`
3. Run the analysis: python master_strategy.py`

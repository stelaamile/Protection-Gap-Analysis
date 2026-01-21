import pandas as pd
import numpy as np

# Data points from your Unipol Internship Report:
# 1. OOP spend is ~23% of total health spending.
# 2. Voluntary Health Insurance (VHI) is only ~2%.
# 3. Coverage: ~40% (North-West) vs ~5% (South/Islands).

regions = {
    'North-West': {'prob': 0.40, 'oop_mean': 600},
    'North-East': {'prob': 0.27, 'oop_mean': 650},
    'Center': {'prob': 0.15, 'oop_mean': 750},
    'South & Islands': {'prob': 0.05, 'oop_mean': 900}
}

data = []
for region, params in regions.items():
    for _ in range(250): # 1000 total customers
        # High OOP spend correlates with SSN waiting lists (Responsiveness)
        oop_spend = np.random.normal(params['oop_mean'], 200)
        has_vhi = np.random.choice([1, 0], p=[params['prob'], 1-params['prob']])
        
        data.append({
            'Region': region,
            'Customer_ID': f"CID_{np.random.randint(10000, 99999)}",
            'Customer_Age': np.random.randint(25, 85), # Variabile demografica
            'Household_Income': np.random.normal(30000, 10000), # Capacità di spesa
            'Has_Health_Insurance': has_vhi,
            'Annual_OOP_Spending': round(max(0, oop_spend), 2),
            'Has_Motor_Insurance': 1, # Almost all current agency customers 
            'Last_Interaction_Days': np.random.randint(0, 365)
        })

df = pd.DataFrame(data)
df.to_csv('data/insurance_market_data.csv', index=False)
print("CSV generated in data/ folder.")
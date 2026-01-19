# Strategic Welfare Transformation: Closing the Italian Health Protection Gap

## Project Overview
This project presents a **management-oriented, data-driven strategic analysis** of the Italian health insurance market, addressing the structural "Protection Gap" whereby the vast majority of private healthcare expenditure remains **out-of-pocket (OOP)** rather than being intermediated through insurance mechanisms.

The analysis builds directly on **internship research conducted within an Unipol Group insurance agency**, translating institutional evidence and field-level insights into a **practical decision-support tool** for insurance managers and agencies.

Given the lack of access to individual-level customer data, the project relies on a **simulated dataset** whose parameters are grounded in **official sources (OECD, Bank of Italy, WHO)** and empirical observations from the internship experience.

---

## Business Context & Problem
The Italian National Health Service (SSN), structured under a **Beveridge universalistic model**, ensures broad coverage but faces increasing challenges in **responsiveness**, including prolonged waiting times and limited freedom of choice.

As a result:
- Private healthcare expenditure accounts for over **23% of total health spending**
- Voluntary Health Insurance (VHI) represents only **~2%**
- Strong territorial disparities persist, with coverage rates of approximately **40% in the North-West** and **~5% in Southern Italy**

This imbalance results in widespread **financial inefficiency for households** and **missed growth opportunities** for insurers.

---

## Strategic Objectives
The project is structured around three core **management objectives**:

1. **Market Intelligence & Segmentation**  
   Identification of high-potential regional and customer segments by combining OOP spending patterns with insurance coverage gaps.

2. **Operational Transformation**  
   Redesign of the agency operating model, shifting front-office roles from transactional processing to **consultative, value-added advisory activities**.

3. **Digital Enablement**  
   Simulation of a tech-enabled lead generation system using personalized QR codes to support data capture, customer profiling, and automated lead prioritization.

---

## Methodology & Tools
- **Data Analysis & Visualization:** Python (Pandas, Matplotlib) for regional segmentation and protection gap mapping.
- **Data Structuring & Targeting:** SQL for customer prioritization logic and lead selection.
- **Business Modeling:** Scenario-based ROI simulations to evaluate incentive structures and operational impact.

The focus is placed on **interpretability and managerial relevance**, rather than technical complexity.
---

## Repository Structure
- `data/`: Contains the simulated dataset (`insurance_market_data.csv`).
- `scripts/`: Python logic for data generation and strategic analysis.
- `sql/`: Prioritization queries for lead scoring.
- `outputs/`: Visual results and charts.
- `notebooks/`: Exploratory data analysis.

---

## Key Results (Simulated)
- **Customer Targeting:** Identification of the top **20% high-potential customers** currently holding only mandatory motor insurance but exhibiting high OOP healthcare spending.
- **Operational Impact:** Estimated **15–20% increase** in specialist appointments through structured digital data capture.
- **Strategic Insight:** Territorial protection gaps represent scalable opportunities for insurance-led welfare integration.

---

## Managerial Implications
The findings suggest that:
- Insurance agencies can act as **welfare intermediaries**, not merely product distributors.
- Targeted, data-informed advisory models can improve both **customer protection** and **commercial performance**.
- Digital tools enable scalable transformation without undermining regulatory compliance or equity principles.

This project demonstrates how **data analytics can support managerial decision-making** in complex, regulated service environments.

---
## How to Run
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Generate data: `python scripts/data_generator.py`.
4. Run analysis: `python scripts/strategic_analysis.py`.
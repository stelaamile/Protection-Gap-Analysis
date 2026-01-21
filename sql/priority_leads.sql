-- Identify the "High-Potential" cluster:
-- Customers paying for Motor insurance who are overpaying for health OOP 
-- but have NO health coverage yet.

SELECT 
    Customer_ID,
    Region,
    Annual_OOP_Spending,
    Last_Interaction_Days,
    -- Algoritmo di Priorità: 70% Spesa OOP, 30% Recency (prossimità di contatto)
    ((Annual_OOP_Spending / 1500.0) * 0.7 + (1 - Last_Interaction_Days / 365.0) * 0.3) * 100 AS Priority_Score
FROM insurance_market_data
WHERE Has_Health_Insurance = 0 
ORDER BY Priority_Score DESC
LIMIT 50;
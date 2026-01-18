-- Identify the "High-Potential" cluster:
-- Customers paying for Motor insurance who are overpaying for health OOP 
-- but have NO health coverage yet.

SELECT 
    Customer_ID,
    Region,
    Annual_OOP_Spending,
    (Annual_OOP_Spending * 0.15) as Potential_Premium_Saving -- Strategic calculation
FROM insurance_market_data
WHERE Has_Health_Insurance = 0 
  AND Annual_OOP_Spending > 750 -- Above average inefficiency threshold [cite: 97]
ORDER BY Annual_OOP_Spending DESC
LIMIT 50;
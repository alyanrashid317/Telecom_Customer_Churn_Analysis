-- ============================
-- Dataset Verification
-- ============================

SELECT COUNT(*) AS total_rows
FROM churn_analysis.telecom_churn;

SELECT * 
FROM churn_analysis.telecom_churn
LIMIT 5;


-- ============================
-- Core Churn KPIs
-- ============================

-- Overall churn rate
SELECT 
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS churn_rate_percentage
FROM churn_analysis.telecom_churn;

-- Monthly revenue lost due to churn
SELECT 
    ROUND(SUM(MonthlyCharges), 2) AS monthly_revenue_lost
FROM churn_analysis.telecom_churn
WHERE Churn = 'Yes';


-- ============================
-- Churn Segmentation
-- ============================

-- Churn by contract type
SELECT 
    Contract,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS churn_rate
FROM churn_analysis.telecom_churn
GROUP BY Contract
ORDER BY churn_rate DESC;

-- Churn by tenure group
SELECT
    CASE
        WHEN tenure < 12 THEN '0–1 year'
        WHEN tenure BETWEEN 12 AND 24 THEN '1–2 years'
        ELSE '2+ years'
    END AS tenure_group,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS churn_rate
FROM churn_analysis.telecom_churn
GROUP BY tenure_group
ORDER BY churn_rate DESC;

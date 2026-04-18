📊 Telecom Customer Churn Analysis: Data-Driven Retention Strategy
📌 Executive Summary
Customer churn is a critical metric for telecommunications providers. This project identifies the primary drivers of attrition and provides actionable, data-backed recommendations to reduce churn. By analyzing customer demographics, contract types, and service usage, I identified a high-risk segment in the first 12 months of tenure and developed strategies to increase long-term Customer Lifetime Value (LTV).

📈 Dashboard Preview
<p align="center">
<img src="https://github.com/alyanrashid317/Telecom_Customer_Churn_Analysis/blob/main/Insights/Telecom_Customer_Churn_Analysis_Dashboard.png?raw=true" alt="PowerBI Dashboard Preview" width="800">
</p>

🔍 Key Insights & Business Impact
1. Contract Risk: The "Month-to-Month" Trap
Finding: Month-to-month subscribers exhibit a 43% churn rate, representing the highest risk segment.

Implication: Low commitment levels are the primary driver of revenue instability.

2. Service Gap: Fiber Optic Reliability
Finding: Fiber optic users churn at a significantly higher rate than DSL users.

Implication: There is a disconnect between the premium price/expectation of fiber and the actual service experience or perceived value.

3. The "Critical First Year"
Finding: Nearly half (48%) of all churn occurs within the first year of the customer journey.

Implication: Onboarding and early-stage engagement are currently insufficient to build brand loyalty.

💡 Strategic Recommendations
Based on the analysis, I recommend the following three-pillar retention strategy:

Contract Migration Incentives: Launch a "Commitment Credit" program that offers a one-time discount for customers migrating from monthly to annual contracts.

Fiber Optic Value Audit: Conduct a service reliability audit and pricing benchmark for fiber optic segments to address the expectation-reality gap.

Proactive "Early-Life" Engagement: Implement an automated 3-6-9 month "Customer Health Check" to provide personalized offers and support to new users during their highest-risk period.

🛠️ Tech Stack & Methodology
Data Extraction & Cleaning: SQL (Joins, CTEs, Window Functions) for preparing the raw dataset.

Exploratory Data Analysis (EDA): Python (Pandas, Seaborn, Matplotlib) to identify correlations and distribution anomalies.

Interactive Visualization: PowerBI for creating dynamic dashboards that allow stakeholders to drill down into specific customer segments.

📂 Project Structure
Data/: Cleaned dataset used for the final analysis.

SQL/: Scripts for data preparation and key metric calculations.

Python/: Jupyter Notebooks/Scripts for EDA and statistical modeling.

PowerBI/: .pbix file containing the interactive executive dashboard.

Insights/: Documentation of detailed findings and screenshots.

## 🚀 How to Replicate
1. **Database:** Run the scripts in `/SQL` to prepare the schema.
2. **Analysis:** Open the `/Python` scripts to view the statistical breakdown.
3. **Visualization:** Open the `/PowerBI` file to interact with the live dashboard.

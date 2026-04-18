import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Clean visual style
sns.set(style="whitegrid")

# --------------------------
# 1) Load & quick check
# --------------------------
df = pd.read_csv("../data/telecom_churn.csv")

print(df.head())
print("Shape:", df.shape)
print(df.info())

# --------------------------
# 2) Data cleaning
# --------------------------
# TotalCharges can contain blanks; coercing converts invalid values to NaN
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
print("\nMissing values:\n", df.isnull().sum())

# --------------------------
# 3) KPI validation (matches your SQL logic)
# --------------------------
churn_rate = df['Churn'].value_counts(normalize=True) * 100
print("\nChurn Rate (%):\n", churn_rate)

revenue_lost = df.loc[df['Churn'] == 'Yes', 'MonthlyCharges'].sum()
print("\nMonthly Revenue Lost (approx):", round(revenue_lost, 2))

# --------------------------
# 4) Feature engineering: tenure buckets
# --------------------------
df['tenure_bucket'] = pd.cut(
    df['tenure'],
    bins=[0, 12, 24, 72],
    labels=['0–1 year', '1–2 years', '2+ years'],
    right=False
)
print("\nTenure bucket sample:\n", df[['tenure', 'tenure_bucket']].head(10))

# --------------------------
# 5) Aggregations for insights
# --------------------------
churn_by_tenure = (
    df.groupby('tenure_bucket')['Churn']
      .apply(lambda x: (x == 'Yes').mean() * 100)
)

churn_by_internet = (
    df.groupby('InternetService')['Churn']
      .apply(lambda x: (x == 'Yes').mean() * 100)
)

avg_charges_by_internet = (
    df.groupby('InternetService')['MonthlyCharges']
      .mean()
      .round(2)
)

fiber_contract_distribution = (
    df.loc[df['InternetService'] == 'Fiber optic', 'Contract']
      .value_counts(normalize=True) * 100
)

print("\nChurn by tenure bucket (%):\n", churn_by_tenure.round(2))
print("\nChurn by internet service (%):\n", churn_by_internet.round(2))
print("\nAvg monthly charges by internet service:\n", avg_charges_by_internet)
print("\nFiber optic contract distribution (%):\n", fiber_contract_distribution.round(2))

# --------------------------
# 6) Visualizations (create all first, then show once)
# --------------------------

# Churn distribution
plt.figure()
sns.countplot(x='Churn', data=df)
plt.title("Customer Churn Distribution")

# Churn by contract type (mean of True/False = churn rate)
plt.figure()
sns.barplot(x='Contract', y=df['Churn'].eq('Yes'), data=df)
plt.title("Churn Rate by Contract Type")
plt.ylabel("Churn Rate")

# Tenure vs churn
plt.figure()
sns.boxplot(x='Churn', y='tenure', data=df)
plt.title("Tenure vs Churn")

# Churn rate by tenure bucket
plt.figure()
sns.barplot(x=churn_by_tenure.index, y=churn_by_tenure.values)
plt.title("Churn Rate by Tenure Bucket")
plt.ylabel("Churn Rate (%)")
plt.xlabel("Tenure Bucket")

# Churn rate by internet service
plt.figure()
sns.barplot(x=churn_by_internet.index, y=churn_by_internet.values)
plt.title("Churn Rate by Internet Service Type")
plt.ylabel("Churn Rate (%)")
plt.xlabel("Internet Service")

# Avg monthly charges by internet service
plt.figure()
sns.barplot(x=avg_charges_by_internet.index, y=avg_charges_by_internet.values)
plt.title("Average Monthly Charges by Internet Service Type")
plt.ylabel("Average Monthly Charges")
plt.xlabel("Internet Service")

# Contract distribution for fiber optic customers
plt.figure()
sns.barplot(x=fiber_contract_distribution.index, y=fiber_contract_distribution.values)
plt.title("Contract Distribution for Fiber Optic Customers")
plt.ylabel("Percentage of Customers")
plt.xlabel("Contract Type")

# Show all plots together
plt.show()



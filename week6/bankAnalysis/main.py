import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
df = pd.read_csv("nepal_bank_transactions.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Create year_month column
df["year_month"] = df["date"].dt.to_period("M").astype(str)

print(df.head())

monthly = df.groupby("year_month").size()

plt.figure()
plt.plot(monthly.index, monthly.values, marker="o", color="#2E7D32")
plt.title("Monthly Transaction Volume, 2024")
plt.xlabel("Month")
plt.ylabel("Number of Transactions")
plt.xticks(rotation=45)
plt.axvspan("2024-10", "2024-11", color="orange", alpha=0.15, label="Dashain/Tihar season")
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))

plt.plot(
    monthly.index,
    monthly.values,
    marker="o",
    linewidth=2,
)

# Amounts vary hugely by type, so let's look at Cash Withdrawals specifically
withdrawals = df[df["transaction_type"] == "Cash Withdrawal"]

plt.figure()
plt.hist(withdrawals["amount_npr"], bins=20, color="#1565C0", edgecolor="white")
plt.title("Distribution of ATM/Counter Cash Withdrawal Amounts")
plt.xlabel("Amount (NPR)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# boxplot

plt.figure()
sns.boxplot(data=df, x="channel", y="processing_time_ms", hue="channel",
            palette="Set2", legend=False)
plt.title("Processing Time by Channel")
plt.xlabel("Channel")
plt.ylabel("Processing Time (ms)")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()

# Heatmap

pivot = pd.crosstab(df["channel"], df["transaction_status"])

plt.figure()
sns.heatmap(pivot, annot=True, fmt="d", cmap="YlGnBu")
plt.title("Transaction Status by Channel")
plt.ylabel("Channel")
plt.xlabel("Status")
plt.tight_layout()
plt.show()

# 
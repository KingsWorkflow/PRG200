import pandas as pd


df= pd.read_csv("nepal_bank_transactions.csv")

#  Display the first five and last five rows of the DataFrame
first_five_rows = df.head()
last_five_rows = df.tail()

print(f"Features :\n{df.columns}")

print("First five rows of the DataFrame:")
print(first_five_rows)
print("\nLast five rows of the DataFrame:")
print(last_five_rows)

print(f"Row count: {df.shape[0]}, Column count: {df.shape[1]}")


print(f"DataFrame Info:")
print(df.info())

print(f"DataFrame Description:")
print(df.describe())

# select single column
print(f"channel:\n{df['channel'].head()}")

# select multiple columns
print(f"channel and amount:\n{df[['channel', 'amount_npr']].head()}")


# loc

print(f"Rows 0 to 4 and columns 'channel' and 'amount_npr':\n{df.loc[0:4, ['channel', 'amount_npr']]}")

# iloc
print(f"Rows 0 to 4 and columns 0 and 1:\n{df.iloc[0:4]}")


# find total tranctions from ATM

total_atm_transactions = df[(df["channel"] == "ATM") & (df["transaction_status"] == "Success")]["amount_npr"].sum()
print(f"Total ATM transactions: {total_atm_transactions}")


# large fund trransfer

large_fund_transfers = df[(df["amount_npr"] > 50000) & (df["transaction_type"] == "Fund Transfer") & (df["transaction_status"] == "Success")]
print(f"Large fund transfers: {len(large_fund_transfers)}")

# sort top 10 highest-value transactions

top_10_transactions = df.sort_values("amount_npr", ascending=False).head(10)[
    ["transaction_id", "amount_npr", "transaction_type", "channel", "transaction_status"]
]
print(f"Top 10 highest-value transactions:\n{top_10_transactions}")



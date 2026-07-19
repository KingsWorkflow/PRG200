import pandas as pd

ages=pd.Series([22,35,58], name="Age")
max_age=ages.max()
min_age=ages.min()
average_age=ages.mean()
print(ages)
print(f"Max age {max_age}")
print(f"Min age {min_age}")
print(f" Average age {average_age:.2f}")
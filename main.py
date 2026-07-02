import pandas as pd
from pathlib import Path

# tells panda to not truncate columns
pd.set_option('display.max_columns', None)

# using path from pathlib to find csv dataset on desktop
csv_path = Path.home() / "Desktop" / "messycsv" / "ObesityDataSet_raw_and_data.csv"

# reads csv file
df = pd.read_csv(csv_path)

# outputs csv file of what is read
df.info()

# finds duplicate rows and counts it
duplicate_rows = df.duplicated().sum()

print("Duplicate rows found:", duplicate_rows)

# cleaned dataset of duplicates
df_cleaned = df.drop_duplicates()
print("Duplicate rows on cleaned dataset:", df_cleaned.duplicated().sum())

# rounding floats and changing dtypes
df_cleaned['Age'] = df_cleaned['Age'].round(0).astype(int)
df_cleaned['Height'] = df_cleaned['Height'].round(2)
df_cleaned['Weight'] = df_cleaned['Weight'] * 2.20462
df_cleaned['Weight'] = df_cleaned['Weight'].round(2)


print(df_cleaned.sample(n=10))
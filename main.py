import pandas as pd
from pathlib import Path

# Creating the absolute path so read_csv can find the csv directory
csv_path = Path.home() / "Desktop" / "messycsv" / "listings.csv"



df = pd.read_csv(csv_path)

df.info()

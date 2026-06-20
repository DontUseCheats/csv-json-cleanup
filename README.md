# csv-json-cleanup
Read messy CSV/JSON and clean/transform and write clean CSV/JSON back out.

## Note Taking
Throughout creating this project, I'll be note taking any new topics/concepts that I learn.

### panda
Difference between relative and absolute path
    
relative path - works if the script is being run from the same folder as where the csv is

absolute path - uses pathlib and Path.home() to search the machine

I needed to use the absolute path method since the csv file I have is located in a different directory.

    csv_path = pathlib.home() / "Desktop" / "messycsv" / "listings.csv"

    df = pd.read.csv

When using df.info() came across missing values for multiple columns showing as NaN. Used 

    print(df_raw['price'].head(10))
    print(df_raw['price'].dtype)

to look at raw values before dtype conversion. Looking at the column names we verified that the name itself is correct. We also verified that missing values problem comes from the raw CSV file itself. To look at the raw file directly we bypass panda and use terminal command

    head -5 ~/Desktop/messycsv/listings.csv
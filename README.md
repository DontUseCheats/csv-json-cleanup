# csv-cleanup
Cleanup of a messy CSV Includes:

Removing duplicates
Changing dtypes

## Note Taking
Throughout creating this project, I'll be note taking any new topics/concepts that I learn.

Syntaxes Learned

.duplicated().sum() 
.duplicated() finds any duplicate rows while .sum() counts how many duplicate rows

.drop_duplicates() drops any duplicate rows in dataset

.sample(n=x) Randomly displays x amount of random rows in dataset

reassignment of dtypes
-dtype Age of float to int
-Rounded to decimal place of 0 for Age
-Rounded to decimal place of 2 for Weight
-Multiplied Weight by 2.20462 to change from Kilo's to pounds then rounded to decimal place of 2

When changing dtypes a new object is created rather than the original being updated. So reassign the original DataFrame object to its newly created one so the variable always points to the latest version of your data.


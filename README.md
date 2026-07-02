# csv-cleanup
Cleanup of a messy CSV Includes:

Removing duplicates

Changing dtypes

Create new folder and file path directory

Save cleaned dataset to new file path

## Note Taking
Throughout creating this project, I'll be note taking any new topics/concepts that I learn.

Syntaxes Learned

.duplicated().sum() 

.duplicated() finds any duplicate rows while .sum() counts how many duplicate rows

.drop_duplicates() drops any duplicate rows in dataset

.sample(n=x) Randomly displays x amount of random rows in dataset

### Reassignment of dtypes

-dtype Age of float to int

-Rounded to decimal place of 0 for Age

-Rounded to decimal place of 2 for Weight

-Multiplied Weight by 2.20462 to change from Kilo's to pounds then rounded to decimal place of 2

When changing dtypes a new object is created rather than the original being updated. So reassign the original DataFrame object to its newly created one so the variable always points to the latest version of your data.

### Pathlib

new_folder_path = Path.home() / "Desktop" / (new path you want to create)

new_folder_path.mkdir(parents = True, exist_ok = True)

    -Create new variable to hold the new path directory of what folder you want to create that would later on hold the new cleaned csv file

    -Last line parents = True allows the code to create the named directory paths if they don't exist. exist_ok = True skips the FileExistsError and silently passes it if the file path were to exist already

new_file_path = new_folder_path / "(name_of_new_csv_file)"

    -Create another new variable that holds folder path directory variable and name of new csv file that you want to create

df_cleaned.to_csv(new_file_path, index = False)

    -Saving cleaned dataset .to_csv to new file path and index = False removes the panda default of creating a new column numbered from 0 to x


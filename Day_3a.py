# Data cleaning/wrangling.

import pandas as pd

pd.options.display.max_rows = 9999

csv_empty = pd.read_csv("C:\\Users\\IJOMA ADANNA\\Downloads\\dirtydata.csv")


#csv_empty.dropna(inplace=True) - Used for dropping all rows of empty positions in the whole dataset.

print(csv_empty)

a = csv_empty["Duration"].mean()
b = csv_empty["Date"].mode()[0]
c = csv_empty["Calories"].mean()
#csv_empty["Date"].fillna(b, inplace=True) - Used for filling the Date column with mode value from all date column values.

#csv_empty["Date"] = pd.to_datetime(csv_empty["Date"]) - Changing format to date format.
#csv_empty.dropna(subset=["Date"], inplace=True) - Used for dropping all rows of empty positions in the date coumn only of the dataset.
#csv_empty.drop(7, inplace=True) - Used for dropping all row 7 of the dataset.

#csv_empty.loc[28, "Calories"] = 300 - For inputing only position row 28 under Calories column with 300.


#Setting condition for filling up emply positions.
#for x in csv_empty.index:
 #   if csv_empty.loc[x, "Duration"] > 120:
  #      csv_empty.loc[x, "Duration"] = 90

#for x in csv_empty.index:
 #   if csv_empty.loc[x,"Duration"] > 120:
  #      csv_empty.drop(x, inplace=True)

#csv_empty.drop_duplicates(inplace=True) - Deleting the duplicated row.
print(csv_empty)
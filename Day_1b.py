
# Tutorial on Pandas python library.
import numpy as np
import pandas as pd

days = pd.Series(["monday","tuesday", "wednesday"])
print(days)

#days_list = np.array(["monday", "tuesday", "wednesday"])
#print(days_list)
a = [1,2,3,4,5]
print(pd.Series(a))
print(pd.Series([1,2,3,4,5], index=["a", "b", "c", "d", "e"]))

calories = {"Day1":250, "Day2":320, "Day3":450}
energy_spent = pd.Series(calories)
print(energy_spent)

b = {"Amount":[100,160,220], "Profit":[0.1,0.4,0.25]}
c = pd.DataFrame(b, index=['x', 'y', 'z'])
print(c)
print(c.loc[['x','y']])

West_Africa = {"Countries": ["Nigeria", "Ghana", "Bene", "Ivory Coast"],
               "Capital":["Abuja", "Accra", "Cotonou", "Abidjan"],
               "Age":[80, 75, 85, 69], "Population":[100000,45000,72000,36000]}
Table1 = pd.DataFrame(West_Africa, index=[2,4,6,8])
print(Table1)

print(Table1.iloc[2])

print(Table1["Countries"])

print(Table1.at[2,"Capital"])
print(Table1.iat[0,1])
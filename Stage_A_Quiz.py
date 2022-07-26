import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.options.display.max_rows = 9999
pd.options.display.max_columns = 99


hamoye_raw_csv = pd.read_csv(r"C:\Users\IJOMA ADANNA\Downloads\FoodBalanceSheets_E_Africa_NOFLAG.csv", encoding= "latin-1")

sample_data = hamoye_raw_csv.sample(n=50, random_state=5)
#sum_fat = hamoye_raw_csv.groupby("Element")["Element"].count()
#print(sum_fat)
#print(hamoye_raw_csv.describe())

#print(hamoye_raw_csv["Y2016"].isnull().sum())

#correlating_plot = sns.pairplot(data=sample_data)
#plt.show()

#import_quantity = hamoye_raw_csv.groupby("Element")["Import_Quantity"].count()
#print(import_quantity)

#sum_prod = hamoye_raw_csv.groupby("Element")["Y2014"].sum()
#print(sum_prod)

#highest_sum = hamoye_raw_csv.groupby("Element")["Y2018"].sum()
#print(highest_sum)

#total_import = hamoye_raw_csv.groupby("Area")["Y2018"].sum()
#print(total_import)

unique = hamoye_raw_csv["Area"].drop_duplicates()
print(unique.count())

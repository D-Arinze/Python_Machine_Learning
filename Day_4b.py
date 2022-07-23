import pandas as pd

pd.options.display.max_rows = 999999999
pd.options.display.max_columns = 99999

hamoye_csv = pd.read_csv(r"C:\Users\IJOMA ADANNA\Downloads\FoodBalanceSheets_E_Africa_NOFLAG.csv", encoding="latin-1")

print(hamoye_csv.head())

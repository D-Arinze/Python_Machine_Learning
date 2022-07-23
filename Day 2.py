
import pandas as pd
pd.options.display.max_rows = 999999
pd.options.display.max_columns = 10

wealth = {"money" : [3450, 4000, 5000],
          "cars" : ["Bentley", "Mercedes", "Bugatti"],
          "houses" : [7,5,9]}
churah = pd.DataFrame(wealth)
learn = pd.read_csv(r"C:\Users\IJOMA ADANNA\Downloads\data.csv")
#print(learn)

excel_import = pd.read_excel(r"C:\Users\IJOMA ADANNA\Desktop\safety.xlsx")
#print(excel_import)

online_csv = pd.read_csv(r"https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv")
print(online_csv.isnull().sum())



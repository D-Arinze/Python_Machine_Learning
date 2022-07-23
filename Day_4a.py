import pandas as pd

pd.options.display.max_rows = 99999
pd.options.display.max_columns = 99999

raw_csv = pd.read_csv(r"https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv")

#print(raw_csv.groupby("report_year")["report_year"].count())

#splitting a big dataframe into two; raw_csv1 and raw_csv2
raw_csv1 = raw_csv.loc[0:19000].reset_index(drop=True)
raw_csv2 = raw_csv.loc[19000:].reset_index(drop=True)


print(raw_csv1.head(5))

merge = pd.merge(raw_csv1, raw_csv2, how= "inner")
print(merge)



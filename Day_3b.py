import pandas as pd
import matplotlib.pyplot as plt
pd.options.display.max_rows = 9999

raw_excel = pd.read_excel(r"C:\Users\IJOMA ADANNA\Desktop\safety.xlsx")
print(raw_excel)
null_cells = raw_excel.isnull().sum()
dup = raw_excel.duplicated()
correlation = raw_excel.corr()

print(null_cells)
print(dup.sum())
print(correlation)
raw_excel.plot()
plt.show()

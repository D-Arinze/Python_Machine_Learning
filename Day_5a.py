import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.options.display.max_rows = 99999

raw_data = pd.read_csv(r"https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv")
print(raw_data)

raw_plot = sns.barplot(data=raw_data)
raw_plot.set_yscale("log")
raw_plot.set_ylim(1,10000)
plt.xlabel("Fuel consumption")
plt.ylabel("count")

plt.show()

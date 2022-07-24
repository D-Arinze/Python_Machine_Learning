import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.options.display.max_columns = 99

raw_csv = pd.read_csv(r"https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv")

# Defining that the linear progression to be plotted should select 50 random datasets with randomness of 20 (The higher the random_state,
# the more sparse the data is selected). fit_reg=False is used to remove the straight line regression model from the plot,
# while scatter=False is used to remove the scattered plots and leave only the straight line.
sample_reg = raw_csv.sample(n= 50, random_state=20)

regression = sns.regplot(data=sample_reg, x= "report_year", y= "fuel_qty_burned", fit_reg=False)

# pairs and plots columns that show some form of correlation.
sns.pairplot(data=sample_reg)

plt.show()
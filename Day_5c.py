import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

raw_csv = pd.read_csv(r"https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv")
sample_data = raw_csv.sample(n = 50, random_state=4)

# Plotting a boxplot of some dataset sample
#boxplot_chart = sns.boxplot(data=sample_data,x="fuel_type_code_pudl", y="utility_id_ferc1", palette=["m","g"])

# Plotting a boxplot of some dataset sample
kde_plot_chart = sns.kdeplot(data=sample_data, x="fuel_cost_per_unit_burned", color="g", fill=True)

plt.show()
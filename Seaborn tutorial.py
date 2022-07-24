import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



data = {"days":["monday","tuesday","wednesday","thursday","friday"], "transactions":[12299,4320,297,299000,13]}
data_table = pd.DataFrame(data)
print(data_table)

plot = sns.barplot(data=data_table, x= "days", y= "transactions")

# Setting the y axis scale to be logarithmic instead of the normal linear.
plot.set_yscale("log")
# Setting the min and max limit to be displayed on y axis
plot.set_ylim(1,10000)

plt.show()
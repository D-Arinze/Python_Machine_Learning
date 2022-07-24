import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sales_internet = {"Year": [1,2,3,4,5,6,7,8,9], "Sales": [651,762,856,1063,1190,1298,1421,1440,1518],
               "Advertising": [23,26,30,34,43,48,52,57,58]}

sales_table = pd.DataFrame(sales_internet)
print(sales_table)

# Plotting a linear regression plot.
regression = sns.regplot(data=sales_table, x= "Advertising", y= "Sales")

plt.show()


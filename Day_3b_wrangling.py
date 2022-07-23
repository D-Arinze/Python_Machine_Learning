import pandas as pd
import matplotlib.pyplot as plt
pd.options.display.max_rows = 9999

raw_excel = pd.read_excel(r"C:\Users\IJOMA ADANNA\Desktop\safety.xlsx")

# Drop all null cells
raw_excel.dropna(inplace=True)
# Drop all duplicated rows
raw_excel.drop_duplicates(inplace=True)

clean_excel = raw_excel
print(clean_excel)

# SHows normal plot
#clean_excel.plot()

#Shows scattered plot, also entails that Duration and Calories correlate
#clean_excel.plot(kind = "scatter", x = "Duration", y = "Calories")

#Shows scattered plot, also entails that Pulse and Maxpulse correlate
#clean_excel.plot(kind = "scatter", x = "Pulse", y = "Maxpulse")

# Shows bar chart of the Duration
clean_excel.plot(kind = "bar", x = "Duration")

# Shows pie chart of the Duration
clean_excel.plot(kind = "pie", y = "Duration")

# Shows histogram chart depicting mode of Duration
#clean_excel["Duration"].plot(kind = "hist")

plt.show()

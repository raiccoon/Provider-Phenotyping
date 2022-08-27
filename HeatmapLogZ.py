import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from GetColumns import get_columns

# Using z-score data.
df = pd.read_excel('C:\\Users\\apple\\Downloads\\log_zscore_transformed_data.xlsx')

metrics = ["Time in Notes per Day", "Time in Notes per Appointment", "Progress Note Length",
    "Length of Documentation per Appointment", "Note Composition Method by Author - Manual"]

columns = get_columns(metrics)

for s in columns:
    del df[s]
    del df[s + '_log']
del df['SER_CID']

g = sns.heatmap(df, cmap = "coolwarm", xticklabels = False, yticklabels = False)
plt.show(block = True)

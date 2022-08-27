import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from GetColumns import get_columns

# Using z-score data.
df = pd.read_excel('C:\\Users\\apple\\Downloads\\logz_clustered_kmeans_lowest_blocked(final).xlsx')

metrics = ["Time in Notes per Day", "Time in Notes per Appointment", "Progress Note Length",
    "Length of Documentation per Appointment", "Note Composition Method by Author - Manual"]

columns = get_columns(metrics)

for s in columns:
    del df[s]
    del df[s + '_log']

y_labels = df['SER_CID'].tolist() 
del df['SER_CID']

# Currently hard-coded in.
x_labels = ["V13", "V14", "V10", "V1", "V4", "V9", "V7", "V8", "V11", "V6", "V12", "V3", "V2", "V5", "V15"]
g = sns.heatmap(df, cmap = "coolwarm", xticklabels = x_labels, yticklabels = y_labels)
plt.show(block = True)

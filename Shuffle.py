import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
from GetColumns import get_columns

df = pd.read_excel('data\\metrics_log_z.xlsx')
print(df)

metrics = ["Time in Notes per Day", "Time in Notes per Appointment", "Progress Note Length",
    "Length of Documentation per Appointment", "Note Composition Method by Author - Manual"]

columns = get_columns(metrics, suffix = "_log_zscore")

for s in columns:
    df[s + '_shuffled'] = np.random.permutation(df[s].values)

print(df)
df.to_excel('data\\shuffled_metrics_log_z.xlsx')

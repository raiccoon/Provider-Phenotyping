import pandas as pd
from GetColumns import get_columns

# metrics_log: Metric data with log transofmration
df = pd.read_excel('data\\metrics_log.xlsx')
print(df)

# Generate column names with _log tag
metrics = ["Time in Notes per Day", "Time in Notes per Appointment", "Progress Note Length",
    "Length of Documentation per Appointment", "Note Composition Method by Author - Manual"]

columns = get_columns(metrics, suffix="_log")

for s in columns:
    # Generate z-scores. Output to new columns with _zscore tag.
    # Standard deviation is calculated using N, not N - 1.
    # Can be changed by using df.std(ddof = 1).
    df[s + '_zscore'] = (df[s] - df[s].mean()) / df[s].std()
print(df)

df.to_excel('data\\metrics_log_z.xlsx')
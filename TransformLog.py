import pandas as pd
import numpy as np
from GetColumns import get_columns

# raw_data: Raw data extracted from XML file, with empty rows removed
df = pd.read_excel('data\\raw_data.xlsx')
print(df)

# Generate column names
metrics = ["Time in Notes per Day", "Time in Notes per Appointment", "Progress Note Length",
    "Length of Documentation per Appointment", "Note Composition Method by Author - Manual"]

columns = get_columns(metrics)

# Perform log transformation, output to new columns with "_log" tag
# Can be changed by using np.log2.
for s in columns:
    df[s + '_log'] = np.log10(df[s])
print(df)

df.to_excel('data\\log_transformed_data.xlsx')


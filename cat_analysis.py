# Print categorical analysis of provider characteristics
import pandas as pd

# raw_data: raw data extracted from XML file, with empty rows removed
# df = pd.read_excel('data\\raw_data.xlsx', 1)

# characteristics: updated characteristics table with redundant columns removed
df = pd.read_excel('categorical\\characteristics.xlsx')

if len(df.columns) > 2:
    for col in df.columns[2:]:
        print(df[col].value_counts())


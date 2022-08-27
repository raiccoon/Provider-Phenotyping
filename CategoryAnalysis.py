# Print categorical analysis of provider characteristics
import pandas as pd

# categorical_na_removed: categorical data extracted from EPIC Signal, with empty rows removed
# df = pd.read_excel('data\\categorical_na_removed.xlsx')

# characteristics: updated characteristics table with redundant columns removed
df = pd.read_excel('data\\categorical_updated.xlsx')

if len(df.columns) > 2:
    for col in df.columns[2:]:
        print(df[col].value_counts())


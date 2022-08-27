# Remove unnecessary/redundant columns from Characteristics matrix
import pandas as pd

# categorical_na_removed: categorical data extracted from EPIC Signal, with empty rows removed
df = pd.read_excel('data\\categorical_na_removed.xlsx')

# Build dict for dataframe
data = {}
data['SER_CID'] = df['SER_CID']
# Keep two columns - User_type (renamed Provider_type) and Department (renamed Specialty) (crop "CC_UCR_XX_" from Department)
data['Provider_Type'] = df['User_Type']
data['Specialty'] = df['Department'].str[10:]

df2 = pd.DataFrame(data)

df2.to_excel('data\\categorical_updated.xlsx')
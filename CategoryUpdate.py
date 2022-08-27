# Remove unnecessary/redundant columns from Characteristics matrix
import pandas as pd

df = pd.read_excel('data\\raw_data.xlsx', 1)

# Build dict for dataframe
data = {}
data['SER_CID'] = df['SER_CID']
# Keep two columns - User_type (renamed Provider_type) and Department (renamed Specialty) (crop "CC_UCR_XX_" from Department)
data['Provider_Type'] = df['User_Type']
data['Specialty'] = df['Department'].str[10:]

df2 = pd.DataFrame(data)

df2.to_excel('categorical\\characteristics.xlsx')
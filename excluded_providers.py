import pandas as pd

# Collect information on excluded providers

# Read raw data extracted from XML file, before rows with empty cells are removed
mdf = pd.read_excel('categorical\\Data Matrix v1.xlsx')
cdf = pd.read_excel('categorical\\Provider Characteristics v1.xlsx')

# Get list of IDs of providers with any empty cells
null_mdf = mdf[mdf.isnull().any(axis=1)]

idlist = set()
for row in null_mdf.itertuples(index = False):
    idlist.add(row.SER_CID)

# Print ID, Provider Type
for row in cdf.itertuples(index = False):
    if row.SER_CID in idlist:
        print(row.SER_CID, row.User_Type)
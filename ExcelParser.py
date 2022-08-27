import pandas as pd
from GetColumns import get_columns

# Read Excel file as DataFrame
# Path name is relative
# If data is saved as XML file, open in Excel and save as an Excel Workbook (.xlsx) file
df = pd.read_excel('data\\deid_PEPDataDownload_June_2022.xlsx')
# print(df)

df.columns = df.columns.str.replace(" ", "_")

# Metrics of interest, in alphabetical order.
metrics = ["Length of Documentation per Appointment", "Note Composition Method by Author - Manual",
    "Progress Note Length", "Time in Notes per Appointment", "Time in Notes per Day"]

md = {}
cd = {}

for row in df.itertuples(index = False):
    if row.Reporting_Period_Start_Date != '5/29/2022':
        continue

    if row.Metric not in metrics:
        continue
    
    if row.SER_CID not in md:
        md[row.SER_CID] = {}
        cd[row.SER_CID] = {
            'Type': row.Type,
            'Provider_Type': row.Provider_Type,
            'Service_Area': row.Service_Area,
            'Department': row.Department,
            'Specialty': row.Specialty,
            'User_Type': row.User_Type
        }

    md[row.SER_CID][row.Metric.replace(" ", "_") + "_numerator"] = row.Numerator
    md[row.SER_CID][row.Metric.replace(" ", "_") + "_denominator"] = row.Denominator
    md[row.SER_CID][row.Metric.replace(" ", "_") + "_value"] = row.Value
    
mdf = pd.DataFrame.from_dict(md, orient="index")
mdf.to_excel('data\\metrics_raw.xlsx')

cdf = pd.DataFrame.from_dict(cd, orient="index")
cdf.to_excel('data\\categorical_raw.xlsx')

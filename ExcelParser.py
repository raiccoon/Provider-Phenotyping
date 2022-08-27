import pandas as pd

# Read Excel file as DataFrame
# Path name may be different on different computers.
df = pd.read_excel('C:\\Users\\apple\\Downloads\\deid_PEPDataDownload_June_2022_EXCEL.xlsx')
print(df)

# Metrics of interest, in alphabetical order.
a = "Length of Documentation per Appointment"
b = "Note Composition Method by Author - Manual"
c = "Progress Note Length"
d = "Time in Notes per Appointment"
e = "Time in Notes per Day"

vis = []
AN = []
AD = []
AV = []
BN = []
BD = []
BV = []
CN = []
CD = []
CV = []
DN = []
DD = []
DV = []
EN = []
ED = []
EV = []

R1 = []
R2 = []
R3 = []
R4 = []
R5 = []
R6 = []
 
# Iterate over all rows in the DataFrame (sorted by SER CID)
for index, row in df.iterrows():
    if row['Reporting Period Start Date'] != '5/29/2022':
        continue

    if (not row['SER CID'] in vis):
        print('---')
        vis.append(row['SER CID'])
        print(row['Type'] + " " + str(row['SER CID']))
        AN.append(None)
        AD.append(None)
        AV.append(None)
        BN.append(None)
        BD.append(None)
        BV.append(None)
        CN.append(None)
        CD.append(None)
        CV.append(None)
        DN.append(None)
        DD.append(None)
        DV.append(None)
        EN.append(None)
        ED.append(None)
        EV.append(None)
        R1.append(row['Type'])
        R2.append(row['Provider Type'])
        R3.append(row['Service Area'])
        R4.append(row['Department'])
        R5.append(row['Specialty'])
        R6.append(row['User Type'])
        
        
    if (row['Metric'] == a):
        print(row['Metric'] + " " + str(row['Numerator']) + " " + str(row['Denominator']) + " " + str(row['Value']))
        AN.pop()
        AN.append(row['Numerator'])
        AD.pop()
        AD.append(row['Denominator'])
        AV.pop()
        AV.append(row['Value'])
    if (row['Metric'] == b):
        print(row['Metric'] + " " + str(row['Numerator']) + " " + str(row['Denominator']) + " " + str(row['Value']))
        BN.pop()
        BN.append(row['Numerator'])
        BD.pop()
        BD.append(row['Denominator'])
        BV.pop()
        BV.append(row['Value'])
    if (row['Metric'] == c):
        print(row['Metric'] + " " + str(row['Numerator']) + " " + str(row['Denominator']) + " " + str(row['Value']))
        CN.pop()
        CN.append(row['Numerator'])
        CD.pop()
        CD.append(row['Denominator'])
        CV.pop()
        CV.append(row['Value'])
    if (row['Metric'] == d):
        print(row['Metric'] + " " + str(row['Numerator']) + " " + str(row['Denominator']) + " " + str(row['Value']))
        DN.pop()
        DN.append(row['Numerator'])
        DD.pop()
        DD.append(row['Denominator'])
        DV.pop()
        DV.append(row['Value'])
    if (row['Metric'] == e):
        print(row['Metric'] + " " + str(row['Numerator']) + " " + str(row['Denominator']) + " " + str(row['Value']))
        EN.pop()
        EN.append(row['Numerator'])
        ED.pop()
        ED.append(row['Denominator'])
        EV.pop()
        EV.append(row['Value'])

data = {'SER CID': vis,
        'Length of Documentation per Appointment, N': AN, 'Length of Documentation per Appointment, D': AD, 'Length of Documentation per Appointment, V': AV,
        'Note Composition Method by Author - Manual, N': BN, 'Note Composition Method by Author - Manual, D': BD, 'Note Composition Method by Author - Manual, V': BV,
        'Progress Note Length, N': CN, 'Progress Note Length, D': CD, 'Progress Note Length, V': CV,
        'Time in Notes per Appointment, N': DN, 'Time in Notes per Appointment, D': DD, 'Time in Notes per Appointment, V': DV,
        'Time in Notes per Day, N': EN, 'Time in Notes per Day, D': ED, 'Time in Notes per Day, V': EV}
DF = pd.DataFrame(data)
print(DF)
DF.to_excel('deid_PEPDataDownload_June2022_MODIFIED.xlsx')

data2 = {'SER CID': vis,
         'Type': R1,
         'Provider Type': R2,
         'Service Area': R3,
         'Department': R4,
         'Specialty': R5,
         'User Type': R6}
DF2 = pd.DataFrame(data2)
print(DF2)
DF2.to_excel('deid_PEPDataDownload_June2022_MODIFIED2.xlsx')

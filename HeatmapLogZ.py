import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Using z-score data.
df = pd.read_excel('C:\\Users\\apple\\Downloads\\log_zscore_transformed_data.xlsx')

s1 = "Time_in_Notes_per_Day_numerator"
s2 = "Time_in_Notes_per_Day_denominator"
s3 = "Time_in_Notes_per_Day_value"
s4 = "Time_in_Notes_per_Appointment_numerator"
s5 = "Time_in_Notes_per_Appointment_denominator"
s6 = "Time_in_Notes_per_Appointment_value"
s7 = "Progress_Note_Length_numerator"
s8 = "Progress_Note_Length_denominator"
s9 = "Progress_Note_Length_value"
s10 = "Length_of_Documentation_per_Appointment_numerator"
s11 = "Length_of_Documentation_per_Appointment_denominator"
s12 = "Length_of_Documentation_per_Appointment_value"
s13 = "Note_Composition_Method_by_Author___Manual_numerator"
s14 = "Note_Composition_Method_by_Author___Manual_denominator"
s15 = "Note_Composition_Method_by_Author___Manual_value"

columns = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15]
for s in columns:
    del df[s]
    del df[s + '_log']
del df['SER_CID']

g = sns.heatmap(df, cmap = "coolwarm", xticklabels = False, yticklabels = False)
plt.show(block = True)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Using z-score data.
df = pd.read_excel('C:\\Users\\apple\\Downloads\\logz_clustered_kmeans_shuffled_lowest_blocked_shuffled(final).xlsx')

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
    del df[s + '_log_zscore']

y_labels = df['SER_CID'].tolist() 
del df['SER_CID']

# Currently hard-coded in.
x_labels = ["V13", "V14", "V10", "V1", "V4", "V9", "V7", "V8", "V11", "V6", "V12", "V3", "V2", "V5", "V15"]
g = sns.heatmap(df, cmap = "coolwarm", xticklabels = x_labels, yticklabels = y_labels)
plt.show(block = True)

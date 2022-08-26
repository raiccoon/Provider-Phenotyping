import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

df = pd.read_excel('C:\\Users\\apple\\Downloads\\log_zscore_transformed_data.xlsx')
print(df)

s1 = "Time_in_Notes_per_Day_numerator_log_zscore"
s2 = "Time_in_Notes_per_Day_denominator_log_zscore"
s3 = "Time_in_Notes_per_Day_value_log_zscore"
s4 = "Time_in_Notes_per_Appointment_numerator_log_zscore"
s5 = "Time_in_Notes_per_Appointment_denominator_log_zscore"
s6 = "Time_in_Notes_per_Appointment_value_log_zscore"
s7 = "Progress_Note_Length_numerator_log_zscore"
s8 = "Progress_Note_Length_denominator_log_zscore"
s9 = "Progress_Note_Length_value_log_zscore"
s10 = "Length_of_Documentation_per_Appointment_numerator_log_zscore"
s11 = "Length_of_Documentation_per_Appointment_denominator_log_zscore"
s12 = "Length_of_Documentation_per_Appointment_value_log_zscore"
s13 = "Note_Composition_Method_by_Author___Manual_numerator_log_zscore"
s14 = "Note_Composition_Method_by_Author___Manual_denominator_log_zscore"
s15 = "Note_Composition_Method_by_Author___Manual_value_log_zscore"

columns = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15]
for s in columns:
    df[s + '_shuffled'] = np.random.permutation(df[s].values)

print(df)
df.to_excel('log_zscore_transformed_data_shuffled.xlsx')

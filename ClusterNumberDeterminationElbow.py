import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Using transformed data: log transformation + z-score transformation.
df = pd.read_excel('C:\\Users\\apple\\Downloads\\log_zscore_transformed_data.xlsx')
# print(df)

IDList = []
for row in df.itertuples(index = False):    
    IDList.append(row.SER_CID)
# print(IDList)

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
data = []
for index, row in df.iterrows():
    lst = []
    for s in columns:
        lst.append(row[s])

    data.append(lst)
# print(data)
arr = np.array(data)

sse = {}
for numClusters in range(1, 10):
    kmeans = KMeans(n_clusters = numClusters).fit(arr)
    clusters = kmeans.labels_
    print(clusters)

    clustered = []
    for i in range(numClusters):
        clustered.append([])
    for i in range(len(IDList)):
        clustered[clusters[i]].append(IDList[i])

    for i in range(numClusters):
        print('Cluster:', i)
        print(clustered[i])

    sse[numClusters] = kmeans.inertia_
    print('SSE:', kmeans.inertia_)
    print('===')

plt.figure()
plt.plot(list(sse.keys()), list(sse.values()))
plt.xlabel("Number of clusters")
plt.ylabel("SSE")
plt.show()

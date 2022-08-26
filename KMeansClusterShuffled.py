import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

# Using z-score data.
df = pd.read_excel('C:\\Users\\apple\\Downloads\\log_zscore_transformed_data_shuffled.xlsx')
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
        lst.append(row[s + "_shuffled"])

    data.append(lst)
# print(data)
arr = np.array(data)

numClusters = 4
kmeans = KMeans(n_clusters = numClusters).fit(arr)
clusters = kmeans.labels_
# print(clusters)

clustered = []
for i in range(numClusters):
    clustered.append([])
for i in range(len(IDList)):
    clustered[clusters[i]].append(IDList[i])

reindexed = []
for i in range(numClusters):
    print('Cluster:', i)
    print(clustered[i])
    reindexed = reindexed + clustered[i]

sse = kmeans.inertia_
print('SSE:')
print(sse)

new_index = []
for i in range(len(reindexed)):
    new_index.append(df[df['SER_CID'] == reindexed[i]].index[0])
df_clustered = df.reindex(new_index)
print(df_clustered)

df_clustered.to_excel('logz_clustered_kmeans_shuffled.xlsx')




    
    




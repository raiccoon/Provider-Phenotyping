import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
from GetColumns import get_columns

# Using z-score data.
df = pd.read_excel('data\\metrics_log_z.xlsx')
# print(df)

IDList = []
for row in df.itertuples(index = False):    
    IDList.append(row.SER_CID)
# print(IDList)

metrics = ["Time in Notes per Day", "Time in Notes per Appointment", "Progress Note Length",
    "Length of Documentation per Appointment", "Note Composition Method by Author - Manual"]

columns = get_columns(metrics, suffix = "_log_zscore")

data = []
for index, row in df.iterrows():
    lst = []
    for s in columns:
        lst.append(row[s])

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

df_clustered.to_excel('data\\clustered_kmeans_log_z.xlsx')




    
    




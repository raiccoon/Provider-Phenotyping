import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
from GetColumns import get_columns

# Using z-score data.
df = pd.read_excel('data\\metrics_log_z.xlsx')
# print(df)

metrics = ["Time in Notes per Day", "Time in Notes per Appointment", "Progress Note Length",
    "Length of Documentation per Appointment", "Note Composition Method by Author - Manual"]

columns = get_columns(metrics, suffix = "_log_zscore")

IDList = []
data = []
for index, row in df.iterrows():
    IDList.append(int(row.SER_CID))
    lst = []
    for s in columns:
        lst.append(row[s])

    data.append(lst)
arr = np.array(data)

# Cluster analysis
numClusters = 4
kmeans = KMeans(n_clusters = numClusters).fit(arr)
clusters = kmeans.labels_
df['Cluster'] = clusters

# Print information about clusters
clustered = []
for i in range(numClusters):
    clustered.append([])
for i in range(len(IDList)):
    clustered[clusters[i]].append(IDList[i])
for i in range(numClusters):
    print('Cluster:', i)
    print(clustered[i])

sse = kmeans.inertia_
print('SSE:', sse)

# Output data sorted by cluster
# Sheet name includes SSE to run clustering multiple times, save sheets separately, and compare afterward
# SSE is rounded to 10ths place, decimal point removed
df = df.sort_values(by=['Cluster'])
df.to_excel('data\\clustered_kmeans_{}.xlsx'.format((int(sse*10))))

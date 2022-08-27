import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from GetColumns import get_columns

# Using transformed data: log transformation + z-score transformation.
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

import pandas as pd

# Clustered data with lowest SSE after 10 trials
df = pd.read_excel('data\\clustered_kmeans_1938.xlsx')
# Categorical data for analysis within clusters
cdf = pd.read_excel('data\\categorical_updated.xlsx')

df = df.merge(cdf, on="SER_CID", validate="one_to_one")

df.to_excel("data\\cluster_categorical.xlsx")

numClusters = 4

for i in range(numClusters):
    cluster = df[df['Cluster'] == i]
    print ("Cluster", i)

    # Output non-transformed summary statistics of variables of interest
    print(cluster.Length_of_Documentation_per_Appointment_value.describe())
    print(cluster.Length_of_Documentation_per_Appointment_denominator.describe())
    print(cluster.Time_in_Notes_per_Appointment_value.describe())

    # Output external/categorical statistics
    print(cluster.Provider_Type.value_counts())
    print(cluster.Specialty.value_counts())


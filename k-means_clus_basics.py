# https://www.kaggle.com/parag131/credit-card-k-means-agglomerative-clustering

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

#data
data=pd.read_csv(r'/home/ram/Downloads/kaggle/CC GENERAL.csv')
print(data.info())
print(data.isnull().sum())
data=data.drop(columns="CUST_ID")
data["MINIMUM_PAYMENTS"].fillna(data["MINIMUM_PAYMENTS"].mean(),inplace=True)
data["CREDIT_LIMIT"].fillna(data["CREDIT_LIMIT"].mean(),inplace=True)
print(data.isnull().sum())
print(data.shape)

# We scale the data because it helps to normalise the data within a particular
# range and every feature transforms to a common scale.

from scipy.stats import zscore

data_scaled=data.apply(zscore)
print(data_scaled.head())

# clustering: K means

cluster_range = range(1,15)
cluster_errors=[]
for i in cluster_range:
    clusters=KMeans(i)
    clusters.fit(data_scaled)
    labels=clusters.labels_
    centroids=clusters.cluster_centers_,3
    cluster_errors.append(clusters.inertia_)
clusters_df=pd.DataFrame({'num_clusters':cluster_range,'cluster_errors':cluster_errors})
print(clusters_df)

plt.plot(clusters_df.num_clusters,clusters_df.cluster_errors,marker='o')
plt.xlabel("num_clusters")
plt.ylabel("cluster_errors")

plt.show()

# Choosing k=4 as after k=4 , the cluster errors are almost
# similar and also, the slope of the line is almot constant as well.

kmc=KMeans(4)
kmc.fit(data_scaled)
labels=kmc.labels_


data=pd.concat([data, pd.DataFrame({'cluster':labels})], axis=1)
print(data.head())


print(data.groupby('cluster').mean())

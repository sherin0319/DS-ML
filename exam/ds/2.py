import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

customer=pd.read_csv("customer_data.csv")
points=customer.iloc[:,3:5].values
x=points[:,0]
y=points[:,1]
customer.head()
plt.scatter(x,y,s=50,alpha=0.7)
plt.xlabel=["Annual income (k$)"]
plt.ylabel=["spending"]
kmeans=KMeans(n_clusters=6)
kmeans.fit(points)
prediction_cluster_index=kmeans.predict(points)
plt.scatter(x,y,c=prediction_cluster_index,s=50,alpha=0.7,cmap='viridis')
centers=kmeans.cluster_centers_
#plt.scatter(centers[:,0],centers[:,1], c='red', s='100')
plt.show()






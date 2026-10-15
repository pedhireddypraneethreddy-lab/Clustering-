import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Dataset
data = {
    "Study_Hours": [2, 3, 4, 5, 6, 7, 8, 2, 3, 4],
    "Marks": [50, 55, 65, 70, 80, 85, 90, 45, 55, 60]
}
df = pd.DataFrame(data)

# Features
X = df[["Study_Hours", "Marks"]]

# KMeans model
model = KMeans(n_clusters=2, random_state=0)
model.fit(X)

# Cluster labels
df["Cluster"] = model.labels_
print(df)

# Visualization
plt.scatter(df["Study_Hours"], df["Marks"], c=df["Cluster"])
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("K-Means Clustering")
plt.show()

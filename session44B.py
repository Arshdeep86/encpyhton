from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
irisData = load_iris()
features = irisData.data
print(features)
clusters = 3
# Create the model
model = KMeans(n_clusters=clusters)

# train the model
model.fit(features)

predictions = model.predict(features)
print(predictions)
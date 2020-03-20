from sklearn.cluster import KMeans
bike1 = [200, 100]
car1 = [800,800]

data = [
        bike1, [250, 200], [300, 300], [350, 350],
        car1, [1000, 1100], [1200, 1300], [1500, 1550]
    ]

targetNames = ["car","bike"]

# creating the model
clusters = 2
model = KMeans(n_clusters=clusters)

model.fit(data)

#predictions = model.predict(data)
#print(predictions)
sampleInput = [1190,1170]
predictedClass = model.predict([sampleInput])
print(targetNames[predictedClass[0]])
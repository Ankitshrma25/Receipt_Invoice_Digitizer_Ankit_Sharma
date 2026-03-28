import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Sample data
X = np.array([[1,2],
              [2,3],
              [3,3],
              [6,5],
              [7,7],
              [8,6]])

y = np.array([0,0,0,1,1,1])

# Create model
knn = KNeighborsClassifier(n_neighbors=3)

# Train model
knn.fit(X, y)

# Predict new point
prediction = knn.predict([[4,4]])

print("Prediction:", prediction)
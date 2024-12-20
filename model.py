from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
import pickle

# Load data
data = load_iris()
X, y = data.data, data.target

# Train model
clf = RandomForestClassifier()
clf.fit(X, y)

# Save the model
with open("app/model.pkl", "wb") as f:
    pickle.dump(clf, f)

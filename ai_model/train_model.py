# Script for training ML model
# AI Risk Engine: Model Training
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Example: Load data (replace with your dataset)
data = pd.DataFrame({
    'feature1': [1, 2, 3, 4],
    'feature2': [0, 1, 0, 1],
    'label':    [0, 1, 0, 1]
})

X = data[['feature1', 'feature2']]
y = data['label']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, 'model.pkl')

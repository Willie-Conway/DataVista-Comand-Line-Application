import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# Generate a sample dataset
np.random.seed(42)
X = np.random.rand(100, 2) * 100  # Features
y = X[:, 0] * 0.5 + X[:, 1] * 0.2 + np.random.rand(100) * 10  # Target with some noise

# Create a DataFrame
data = pd.DataFrame(X, columns=['Feature1', 'Feature2'])
data['Target'] = y

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data[['Feature1', 'Feature2']], data['Target'], test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model to a file
model_filename = 'linear_regression_model.joblib'
joblib.dump(model, model_filename)

print(f"Model saved to {model_filename}")

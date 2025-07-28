# train_model.py
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

# Load dataset
df = pd.read_csv('train.csv')

# Select relevant features
features = ['GrLivArea', 'BedroomAbvGr', 'FullBath']  # square footage, bedrooms, bathrooms
X = df[features]
y = df['SalePrice']

# Handle missing values (if any)
X = X.fillna(X.mean())
y = y.fillna(y.mean())

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")
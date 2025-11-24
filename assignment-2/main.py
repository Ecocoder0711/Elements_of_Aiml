import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# --- 1. Load Data ---
df = pd.read_csv('Movie_dataset.csv')

# --- 2. Data Preprocessing ---
# Check for missing values
print("Missing values before processing:\n", df.isnull().sum())

# Drop irrelevant columns for prediction (IDs and Names)
df_clean = df.drop(['movie_id', 'movie_title'], axis=1)

# --- 3. Feature Engineering ---
# Calculate 'movie_age' (Current Year - Release Year)
current_year = 2024
df_clean['movie_age'] = current_year - df_clean['release_year']
df_clean = df_clean.drop('release_year', axis=1)

# One-Hot Encode Categorical Variables ('genre')
df_processed = pd.get_dummies(df_clean, columns=['genre'], drop_first=True)

print("Processed Columns:", df_processed.columns)

# --- 4. Model Training ---
X = df_processed.drop('imdb_rating', axis=1)
y = df_processed['imdb_rating']

# Split into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# --- 5. Model Evaluation ---
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("-" * 30)
print("Model Performance Metrics:")
print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
print(f"R2 Score: {r2:.4f}")
print("-" * 30)

# Compare Actual vs Predicted
comparison = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(comparison)

# --- 6. Visualization ---
plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test, y=y_pred)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2)
plt.xlabel('Actual IMDB Rating')
plt.ylabel('Predicted IMDB Rating')
plt.title('Linear Regression: Actual vs Predicted Ratings')
plt.show()
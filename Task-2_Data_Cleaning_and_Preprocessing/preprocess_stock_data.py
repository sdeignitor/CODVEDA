import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import RobustScaler
from sklearn.ensemble import IsolationForest

# Load the dataset
df = pd.read_csv("C:/Users/aryan/Desktop/CODVED/Task-2_Data_Cleaning_and_Preprocessing/stock_prices.csv")

# Step 1: Parse dates using correct column name 'date'
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df = df.dropna(subset=['date'])  # Drop rows where date couldn't be parsed
df.set_index('date', inplace=True)

# Step 2: Handle missing values
df = df.infer_objects(copy=False)  # Try converting object columns if possible

# Interpolate only numeric columns (prevents warnings from non-numeric ones)
df[df.select_dtypes(include=[np.number]).columns] = df.select_dtypes(include=[np.number]).interpolate(method='time')



# Step 3: Detect and remove outliers using Isolation Forest
iso = IsolationForest(contamination=0.01, random_state=42)
outliers = iso.fit_predict(df[['close']])
df['Outlier'] = outliers
df = df[df['Outlier'] == 1].drop(columns='Outlier')

# Step 4: Feature engineering (Date-based)
df['Day'] = df.index.day
df['Month'] = df.index.month
df['DayOfWeek'] = df.index.dayofweek

# Step 5: Normalize numerical columns
scaler = RobustScaler()
cols_to_scale = ['open', 'high', 'low', 'close', 'volume']
df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])

# Save the final cleaned data
# Optional: Keep only last 1000 rows (or less if needed)
df = df.tail(1000)

# Save with reduced precision to lower file size
df.to_csv("stock_data_cleaned.csv", index=True, float_format="%.4f")



print("✅ Preprocessing complete! Cleaned data saved as 'stock_data_cleaned.csv'")
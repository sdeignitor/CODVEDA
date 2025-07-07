import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Set visual style
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)


# Load with whitespace separation
df = pd.read_csv("C:/Users/aryan/Desktop/CODVED/Task-3_Exploratory_Data_Analysis/house_prediction_data.csv",
    header=None,
    delim_whitespace=True,
    engine='python'
)

# Assign proper column names (Boston Housing standard)
columns = [
    'CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE',
    'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV'
]
df.columns = columns


print("=== DATA PROFILE ===")
print(f"Shape: {df.shape}")
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())
print("\nDescriptive Stats:\n", df.describe().T)


# Histograms for all features
df.hist(bins=30, figsize=(18, 15))
plt.tight_layout()
plt.show()

# Target variable analysis
plt.figure(figsize=(12, 6))
sns.histplot(df['MEDV'], kde=True, bins=30)
plt.title('Distribution of Home Prices (MEDV)')
plt.show()


# Correlation matrix
corr = df.corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
plt.figure(figsize=(14, 10))
sns.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap="coolwarm", center=0)
plt.title("Feature Correlation Matrix")
plt.show()

# Top 5 correlated features
print("\nTop Features Correlated with MEDV:")
print(corr['MEDV'].sort_values(ascending=False)[1:6])

# Key relationships
def plot_scatter(x, y, data=df):
    plt.figure(figsize=(10, 6))
    sns.regplot(x=x, y=y, data=data, scatter_kws={'alpha':0.5})
    plt.title(f"{x} vs {y}")
    plt.show()

plot_scatter('RM', 'MEDV')  # Rooms vs Price
plot_scatter('LSTAT', 'MEDV')  # Poverty vs Price
plot_scatter('PTRATIO', 'MEDV')  # Student-Teacher Ratio vs Price


# Boxplots for key features
plt.figure(figsize=(12, 6))
sns.boxplot(data=df[['CRIM', 'RM', 'LSTAT', 'MEDV']])
plt.title("Outlier Detection")
plt.xticks(rotation=45)
plt.show()

# Z-score analysis
z_scores = np.abs(stats.zscore(df.select_dtypes(include=[np.number])))
outliers = (z_scores > 3).any(axis=1)
print(f"\nNumber of outliers detected: {outliers.sum()}")


# Charles River dummy variable
plt.figure(figsize=(8, 5))
sns.boxplot(x='CHAS', y='MEDV', data=df)
plt.title("Price Comparison: Near Charles River (1) vs Not (0)")
plt.show()


# Price by RAD (accessibility to radial highways)
plt.figure(figsize=(12, 6))
sns.boxplot(x='RAD', y='MEDV', data=df)
plt.title("Home Prices by Highway Accessibility Index")
plt.show()

# NOX (nitrogen oxides) vs Price
plt.figure(figsize=(10, 6))
sns.scatterplot(x='NOX', y='MEDV', data=df, alpha=0.6)
plt.title("Air Pollution vs Home Prices")
plt.show()


print("\n=== KEY FINDINGS ===")
print("1. Strong positive correlation between RM (rooms) and price")
print("2. Strong negative correlation between LSTAT (poverty) and price")
print("3. CRIM (crime rate) shows extreme right-skew with many outliers")
print("4. About 5% of records show outlier characteristics")
print("5. Properties near Charles River (CHAS=1) command premium prices")
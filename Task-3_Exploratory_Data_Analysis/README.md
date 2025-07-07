# House Price Prediction - Exploratory Data Analysis (EDA)

Comprehensive exploratory data analysis of a house price prediction dataset, identifying key patterns, correlations, and insights to inform predictive modeling.


## 📊 Dataset Information

**Source**: Modified Boston Housing Dataset  
**Features**: 13 predictive attributes  
**Target**: MEDV (Median home value in $1000s)  
**Records**: 505  
**Original Columns**:
- CRIM: Per capita crime rate
- ZN: Proportion of residential land zoned for large lots
- INDUS: Proportion of non-retail business acres
- CHAS: Charles River dummy variable (1 if tract bounds river, 0 otherwise)
- NOX: Nitric oxides concentration
- RM: Average number of rooms per dwelling
- AGE: Proportion of owner-occupied units built prior to 1940
- DIS: Weighted distances to employment centers
- RAD: Index of accessibility to radial highways
- TAX: Property tax rate
- PTRATIO: Pupil-teacher ratio
- B: Black population proportion
- LSTAT: % lower status population

## 🔍 Key Findings

1. **Strong Correlations**:
   - Positive: RM (rooms) → +0.7 with MEDV
   - Negative: LSTAT (poverty) → -0.74 with MEDV

2. **Outliers Detected**:
   - 5% records showed abnormal values (Z-score > 3)
   - Extreme right-skew in crime rate (CRIM) distribution

3. **Premium Pricing Factors**:
   - Homes near Charles River (CHAS=1) priced 28% higher
   - Each additional room (RM) adds ~$9,000 to home value

4. **Negative Influences**:
   - High LSTAT areas show 40% price depression
   - Pollution (NOX) levels inversely correlate with price

## 📈 Visualization Highlights

| Analysis Type | Example Visualization |
|--------------|-----------------------|
| Distribution | ![MEDV Histogram](images/medv_dist.png) |
| Correlation  | ![Heatmap](images/corr_matrix.png) |
| Relationships| ![RM vs Price](images/rm_medv.png) |
| Outliers     | ![Boxplots](images/outliers.png) |


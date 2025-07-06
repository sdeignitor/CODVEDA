# Task 2: Data Cleaning and Preprocessing

### ✅ Internship: Data Science @ Codveda Technologies  
### 🧠 Objective: Clean and preprocess a raw stock prices dataset to make it suitable for analysis or modeling.

---

## 📂 Dataset Used
- **File**: `stock_prices.csv`
- **Columns**: `['symbol', 'date', 'open', 'high', 'low', 'close', 'volume']`

---

## ⚙️ Preprocessing Steps Applied

1. **Parse Dates**
   - Converted `date` column to datetime format
   - Set it as the index for time-based operations

2. **Handle Missing Values**
   - Time-based interpolation for numerical columns

3. **Outlier Detection**
   - Used `IsolationForest` to detect and remove anomalous `close` prices

4. **Feature Engineering**
   - Extracted `Day`, `Month`, `DayOfWeek` from `date` index

5. **Scaling**
   - Applied `RobustScaler` to normalize price and volume data

---

## 🛠️ Tools & Libraries
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn

---

## 📄 Output
- Final file: `stock_data_cleaned.csv`
- Ready for machine learning tasks like forecasting, classification, clustering, etc.

---

## 📊 Visualizations (see Notebook)
- Heatmaps of correlation
- Outlier plots
- Trends over time

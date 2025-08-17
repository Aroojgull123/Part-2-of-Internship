# ⚡ Energy Consumption Time Series Forecasting

## 🎯 Objective  
Forecast short-term household energy consumption using historical time-based data to support smarter energy planning and efficiency.

---

## 📊 Dataset  
**Dataset Used:** `energydata_complete.csv`  
This dataset includes features such as:
- Date and time (`date`)
- Energy usage in appliances (`Appliances`)
- Indoor and outdoor temperature readings
- Humidity levels
- Weather-related conditions

---

## 📝 Project Overview  
This project leverages time series forecasting techniques to model and predict hourly appliance energy consumption. It explores and compares traditional statistical models with modern machine learning and deep forecasting approaches.

---

## ✅ Steps Performed

### 1. 📁 **Data Loading and Preprocessing**
- Loaded the dataset from CSV format using Google Colab.
- Converted the `date` column into datetime format and set it as the index.
- Resampled data to hourly averages.
- Forward-filled missing values.
- Focused on the target variable: **`Appliances`** energy consumption.

### 2. 🔧 **Feature Engineering**
- Created time-based features:
  - Hour of day
  - Day of week
  - Weekend vs weekday
- Prepared training and testing splits based on time (80% train, 20% test).

### 3. 🧠 **Model 1: ARIMA**
- Fitted an ARIMA model on the training time series.
- Forecasted appliance usage on the test period.
- Evaluated with MAE and RMSE.

### 4. 📈 **Model 2: Prophet**
- Reformatted data to Prophet's requirements (`ds` and `y`).
- Used hourly frequency to generate future predictions.
- Extracted forecast results and evaluated model performance.

### 5. 🚀 **Model 3: XGBoost**
- Used time-based features (`hour`, `dayofweek`, `is_weekend`) as inputs.
- Trained an XGBoost Regressor on the engineered features.
- Predicted and evaluated performance on the test set.

### 6. 📊 **Model Evaluation & Comparison**
- Compared models using:
  - **MAE** (Mean Absolute Error)
  - **RMSE** (Root Mean Squared Error)
- Visualized **actual vs predicted** appliance energy consumption for each model.

---

## 📉 Results Summary

| Model     | MAE   | RMSE  |
|-----------|-------|--------|
| ARIMA     | ✅    | ✅     |
| Prophet   | ✅    | ✅     |
| XGBoost   | ✅    | ✅     |

📌 (Exact values depend on execution — shown in notebook output)

---

## 🛠️ Skills Gained
- ✅ Time series analysis and forecasting  
- ✅ Data resampling and time parsing  
- ✅ Feature engineering for temporal data  
- ✅ ARIMA, Prophet, and XGBoost implementation  
- ✅ Model evaluation with MAE & RMSE  
- ✅ Forecast visualization

---

## 📌 How to Use This Project
1. Upload the `energydata_complete.csv` dataset.
2. Run the preprocessing and resampling steps.
3. Train and evaluate each forecasting model.
4. Compare their performance visually and numerically.
5. Use the best-performing model for short-term energy predictions.

---

## 📎 Future Enhancements
- Incorporate additional features (temperature, humidity, etc.) into the models.
- Explore LSTM/GRU deep learning models for sequential learning.
- Deploy the best model as an API for real-time prediction.

---

## ✅ Final Note
This project demonstrates how time series forecasting can be used to predict household energy consumption using historical patterns. It combines classical statistical techniques and machine learning for better performance insights.


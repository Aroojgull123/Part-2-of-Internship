# 🏦 Loan Default Risk with Business Cost Optimization

## 🎯 Objective
Predict the likelihood of loan default and optimize the classification threshold based on a business cost-benefit analysis to minimize financial losses.

---

## 📊 Dataset
**Home Credit Default Risk Dataset**  
This dataset contains extensive information on borrowers’ credit history and financial behavior to support credit risk assessment.

---

## 📝 Project Overview
This project focuses on building binary classification models to predict loan default risk. It incorporates business costs associated with false positive and false negative predictions to optimize the decision threshold, ensuring the model’s outputs are aligned with real-world financial impact.

---

## ✅ Steps Performed

### 1. 📁 **Data Loading and Cleaning**
- Loaded dataset from CSV files.
- Handled missing values and inconsistent data.
- Encoded categorical variables where necessary.

### 2. 🔍 **Exploratory Data Analysis (EDA)**
- Investigated feature distributions and target balance.
- Visualized relationships between features and default risk.

### 3. ⚙️ **Feature Engineering & Preprocessing**
- Selected relevant features based on domain knowledge and correlation analysis.
- Applied scaling techniques where needed.

### 4. 🏋️ **Model Training**
- Trained multiple binary classification models including:
  - Logistic Regression  
  - CatBoost Classifier  
- Tuned hyperparameters and improved convergence through scaling and iteration adjustments.

### 5. 📊 **Feature Importance**
- Extracted feature importances from CatBoost to interpret key drivers of loan default risk.
- Visualized the top 10 influential features with bar plots.

### 6. 💰 **Business Cost Optimization**
- Defined custom costs for:
  - False Positives (e.g., rejecting a good borrower)  
  - False Negatives (e.g., approving a risky borrower)  
- Computed total business cost for a range of classification thresholds.
- Identified the optimal threshold minimizing the total cost.
- Visualized cost vs. threshold to analyze trade-offs.

### 7. 📈 **Final Evaluation**
- Applied the optimized threshold to generate final predictions.
- Reported classification metrics such as precision, recall, F1-score.
- Provided a clear summary of business impact and model performance.

---

## 🛠️ Skills Gained
- ✅ Binary classification modeling with logistic regression and CatBoost  
- ✅ Handling class imbalance and feature preprocessing  
- ✅ Business-aware threshold optimization  
- ✅ Cost-sensitive evaluation metrics  
- ✅ Feature importance extraction and interpretation  
- ✅ Data visualization for model insights

---

## 📌 How to Use This Project

1. Download and unzip the **Home Credit Default Risk Dataset** from [Kaggle](https://www.kaggle.com/datasets/laotse/credit-risk-dataset).
2. Load the data using pandas and perform preprocessing.
3. Train your classification models (Logistic Regression, CatBoost).
4. Define business costs for false positives and false negatives relevant to your use case.
5. Sweep decision thresholds, calculate the total business cost for each, and select the optimal threshold.
6. Evaluate and interpret the model results at the optimized threshold.
7. Visualize feature importance and cost vs threshold plots to understand model decisions.

---

## 📎 Future Enhancements (Optional)
- Incorporate more advanced feature engineering and selection techniques.
- Use cross-validation for more robust threshold tuning.
- Extend cost modeling to multi-class or regression scenarios.
- Deploy a real-time scoring system with business cost monitoring.

---

## ✅ Final Note
This project bridges the gap between machine learning predictions and practical business impact by embedding cost-sensitive decision-making into the loan default risk prediction pipeline.

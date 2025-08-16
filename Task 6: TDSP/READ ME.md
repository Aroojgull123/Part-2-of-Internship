# Term Deposit Subscription Prediction (Bank Marketing)  

![Python](https://img.shields.io/badge/python-3.8%2B-blue)  
![Scikit-learn](https://img.shields.io/badge/scikit--learn-0.24-green)  
![Status](https://img.shields.io/badge/status-completed-brightgreen)  

---

## Project Overview  
Predict whether a bank customer will subscribe to a term deposit after a marketing campaign using classification models and explainability techniques.

## Dataset  
Bank Marketing Dataset from UCI ML Repository — customer and campaign info with subscription target.

## Objectives  
- Preprocess and encode data  
- Train Logistic Regression & Random Forest models  
- Evaluate using Accuracy, F1 Score, AUC, Confusion Matrix, and ROC Curve  
- Explain predictions with LIME (or SHAP)  
- Compare model performance  

## Key Results  

| Model               | Accuracy | F1 Score | AUC    |
|---------------------|----------|----------|--------|
| Logistic Regression  | 11.26%   | 20.25%   | 0.50   |
| Random Forest       | 91.83%   | 57.96%   | 0.95   |

*Random Forest outperforms Logistic Regression, showing stronger predictive power.*

## Usage  

### Install dependencies  
```bash
pip install pandas numpy scikit-learn matplotlib seaborn lime shap

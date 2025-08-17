# 🛍️ Customer Segmentation Using Unsupervised Learning

## 🎯 Objective
Segment mall customers based on their spending patterns and demographic information, and propose targeted marketing strategies for each group.

---

## 📊 Dataset
**Mall Customers Dataset**  
The dataset contains customer data including:
- Customer ID  
- Gender  
- Age  
- Annual Income (k$)  
- Spending Score (1–100)

---

## 📝 Project Overview
This project applies unsupervised machine learning techniques to identify meaningful customer segments that can help businesses:
- Personalize marketing efforts  
- Improve customer retention  
- Increase overall revenue

---

## ✅ Steps Performed

### 1. 📁 **Data Loading and Cleaning**
- Uploaded the CSV dataset using Google Colab file upload.
- Handled cases where the file had formatting issues (e.g., extra column headers, separators).
- Renamed `Genre` column to `Gender` for consistency.

### 2. 🔍 **Exploratory Data Analysis (EDA)**
- Checked data types and null values.
- Plotted distributions of:
  - **Age**
  - **Annual Income**
  - **Spending Score**
  - **Gender**
- Gained initial insights about customer demographics and spending behaviors.

### 3. ⚙️ **Feature Selection & Scaling**
- Selected `Annual Income` and `Spending Score` as features for clustering.
- Applied **StandardScaler** to normalize the data.

### 4. 🔢 **K-Means Clustering**
- Used the **Elbow Method** to determine the optimal number of clusters.
- Applied **KMeans** algorithm to segment customers into clusters.
- Assigned cluster labels back to the original dataset.

### 5. 🧬 **Dimensionality Reduction for Visualization**
#### a. **PCA (Principal Component Analysis)**
- Reduced 2D data into principal components for easy visualization.
- Plotted clusters using PCA components.

#### b. **t-SNE (t-distributed Stochastic Neighbor Embedding)**
- Used t-SNE to capture complex, non-linear relationships in the data.
- Visualized the clusters in 2D space using t-SNE results.

### 6. 📈 **Customer Segment Analysis**
- Analyzed the characteristics of each cluster:
  - Income level
  - Spending behavior
- Interpreted segments such as:
  - High-income, high-spending customers
  - Low-income, high-spending customers
  - High-income, low-spending customers, etc.

### 7. 💡 **Marketing Strategy Recommendations**
Suggested customized strategies for each segment, for example:
- **Premium Offers** for high-spending clients
- **Discount Campaigns** for budget-conscious customers
- **Brand Awareness** for low-engagement, high-income users

---

## 🛠️ Skills Gained
- ✅ Unsupervised learning: K-Means clustering  
- ✅ Dimensionality reduction: PCA and t-SNE  
- ✅ Data visualization using seaborn & matplotlib  
- ✅ Customer segmentation and behavioral analysis  
- ✅ Data-driven marketing strategy development

---

## 📌 How to Use This Project

1. Upload the `Mall_Customers.csv` dataset to your Colab environment.
2. Read and clean the dataset (handle column issues if any).
3. Perform EDA to understand the customer landscape.
4. Scale relevant features (`Annual Income`, `Spending Score`).
5. Use the Elbow Method to decide `k` (number of clusters).
6. Fit a K-Means model on the scaled data.
7. Visualize clusters using both PCA and t-SNE.
8. Analyze each segment and apply marketing strategies based on insights.

---

## 📎 Future Enhancements (Optional)
- Use all features (`Age`, `Gender`, etc.) for multidimensional clustering.
- Evaluate clustering quality using **Silhouette Score**.
- Deploy this model as a customer segmentation tool for marketing teams.

---

## ✅ Final Note
This project demonstrates a complete customer segmentation pipeline using unsupervised learning — from raw data to actionable business insights.


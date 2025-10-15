# 🧠 Customer Churn Prediction — Version 1

## 🚀 Overview
This project predicts whether a customer is likely to **churn** (stop using a service) based on their demographic and subscription data.  
The goal is to help companies **identify at-risk customers early** and take **proactive retention actions** such as targeted offers or service improvements.

This is **Version 1**, focused on building, evaluating, and deploying a production-ready ML model using **Microsoft Azure Machine Learning** with **Managed Online Endpoints** for real-time predictions.

---

## 🎯 Objectives
- Perform data preprocessing and feature encoding  
- Train a machine learning model to predict churn  
- Evaluate the model using standard metrics  
- Deploy it as a REST API on Azure ML  
- Test the endpoint with real-time inference  

---

## 📊 Dataset Description
**Source:** WA_Telecom Customer Churn Dataset  

| Feature Example | Description |
|------------------|-------------|
| gender           | Gender (0 = Male, 1 = Female) |
| SeniorCitizen    | Senior status (1 = Yes, 0 = No) |
| Partner          | Has a partner (1 = Yes, 0 = No) |
| Dependents       | Has dependents (1 = Yes, 0 = No) |
| tenure           | Number of months the customer has stayed |
| PhoneService     | Has phone service (1 = Yes, 0 = No) |
| MultipleLines    | Multiple line service (encoded) |
| InternetService  | Internet provider type (encoded) |
| OnlineSecurity   | Online security service (encoded) |
| OnlineBackup     | Online backup service (encoded) |
| DeviceProtection | Device protection (encoded) |
| TechSupport      | Technical support (encoded) |
| StreamingTV      | Streaming TV service (encoded) |
| StreamingMovies  | Streaming movie service (encoded) |
| Contract         | Type of contract (encoded) |
| PaperlessBilling | Paperless billing (1 = Yes, 0 = No) |
| PaymentMethod    | Payment method (encoded) |
| MonthlyCharges   | Monthly billing amount |
| TotalCharges     | Total amount billed |

**Size:** ~7,000 records  

---

## 🧮 Model Development

**Algorithm:** Random Forest Classifier  

**Why Random Forest?**
- Handles mixed numerical and categorical features well  
- Robust to overfitting  
- Provides feature importance insights  

**Pipeline Steps:**
1. Data cleaning and missing value handling  
2. Feature encoding (`LabelEncoder`, `OneHotEncoder`)  
3. Train-test split (80/20)  
4. Model training and hyperparameter tuning  
5. Model evaluation  
6. Registration and deployment on Azure ML  

---

## 📈 Model Evaluation

| Metric | Score |
|--------|--------|
| Accuracy | 0.87 |
| Precision | 0.82 |
| Recall | 0.79 |
| F1-Score | 0.80 |
| ROC-AUC | 0.91 |

📊 *(Confusion matrix and ROC curve images are stored in `/evaluation/`)*

Example:

evaluation/ ├── confusion_matrix.png └── roc_curve.png

---

## ⚙️ Tech Stack

| Category | Tools |
|-----------|-------|
| **Language** | Python 3.10 |
| **Libraries** | Pandas, NumPy, Scikit-learn, Joblib, JSON |
| **Platform** | Microsoft Azure ML |
| **Deployment** | Azure Managed Online Endpoint |
| **Version Control** | Git + GitHub |

---

## 🌐 Deployment Details
| Attribute | Value |
|------------|--------|
| **Endpoint Name** | `customer-churn-endpoint` |
| **Compute Type** | `Standard_DS1_v2` |
| **Region** | East US |
| **Status** | ✅ Successfully Deployed |

## 🧠 Sample Input & Output

### **Input Example**
The model receives customer data as numerical and categorical features, preprocessed into 19 numeric values. 

````markdown

```json
{
  "data": [[1, 0, 1, 0, 24, 1, 2, 1, 0, 1, 1, 0, 1, 1, 2, 1, 3, 79.85, 1889.5]]
}

````

### **Sample Output**

After processing, the model returns a prediction with the churn probability.

```json
{
  "prediction": "Not Churn",
  "probability": 0.06
}
```

---

## 📂 Project Structure

```
customer-churn/version1/
│
├── data/
│   ├── WA-teleco.csv
│   └── preprocessed.csv
│
├── src/
│   ├── train_model.py
│   └── score.py
│
├── deployment/
│   ├── register_model.py
│   └── deploy_endpoint.py
│
├── evaluation/
│   ├── confusion_matrix.png
│   └── roc_curve.png
│
├── environment/
│   └── conda.yaml
│
└── README.md
```

---

## 🔮 Future Enhancements (Version 2 Roadmap)

1. **SHAP Explainability Dashboard**
   Build an interactive dashboard to visualize feature importance and interpret churn predictions.

2. **Streamlit Frontend**
   Develop a Streamlit web app for real-time predictions and churn risk visualization.

3. **Automated Model Retraining (MLOps)**
   Implement an automated retraining pipeline triggered by new data uploads.

4. **Database Integration**
   Connect with Azure SQL or Cosmos DB for live data access and prediction storage.

---

## 💡 Key Learnings

* Understood the **end-to-end ML lifecycle**: from data collection to deployment.
* Gained experience managing **Azure ML environments, quotas, and compute instances**.
* Improved skills in **model debugging**, **container deployment**, and **Azure integration**.
* Enhanced understanding of **feature engineering** and **business problem framing**.

---

## 👨‍💻 Author

**Victor Isuo**
*Microsoft Certified AI/ML Engineer*

📧 **Email:** [victorisuo1321@gmail.com](mailto:victorisuo@gmail.com)
🔗 **LinkedIn:** [linkedin.com/in/victor-isuo-a02b6171](https://linkedin.com/in/victor-isuo-a02b6171)
💻 **GitHub:** [github.com/Sirvic1321](https://github.com/Sirvic1321)



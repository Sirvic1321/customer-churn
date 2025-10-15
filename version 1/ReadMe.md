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
**Source:** IBM Telco Customer Churn Dataset  

| Feature | Description |
|----------|-------------|
| `gender` | Customer gender (Male/Female) |
| `SeniorCitizen` | Indicates if the customer is a senior |
| `Partner`, `Dependents` | Family and social details |
| `tenure` | Number of months with the company |
| `PhoneService`, `InternetService` | Types of services used |
| `Contract`, `PaymentMethod` | Contract type and payment details |
| `MonthlyCharges`, `TotalCharges` | Billing information |
| `Churn` | Target variable (Yes = 1, No = 0) |

**Size:** ~7,000 records  
**Churn Rate:** ~27%  

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

**Sample Test Input:**
```json
{
  "data": [[1, 0, 35, 1, 0, 70.35, 1, 2, 3, 4, 5]]
}

Sample Output:

{
  "prediction": "Not Churn",
  "probability": 0.06
}


---

📂 Project Structure

customer-churn/version1/
│
├── data/
│ └── customer_churn.csv
│
├── src/
│ ├── train_model.py
│ ├── score.py
│
├── deployment/
│ ├── register_model.py
│ ├── deploy_endpoint.py
│
├── evaluation/
│ ├── confusion_matrix.png
│ └── roc_curve.png
│
├── environment/
│ └── conda.yaml
│
└── README.md


---

🔮 Future Enhancements (Version 2 Roadmap)

1. SHAP Explainability Dashboard
Visualize feature contributions and interpret predictions to understand what drives customer churn.


2. Streamlit Frontend
Build an interactive Streamlit web app that allows users to input customer data, view predictions, and see churn risk in real time.


3. Automated Model Retraining (MLOps)
Implement a retraining pipeline that automatically updates the model when new data is uploaded.


4. Database Integration
Connect with Azure SQL or Cosmos DB for live data retrieval and prediction storage.




---

💡 Key Learnings

Understood end-to-end ML lifecycle: data → training → deployment → inference

Learned how to manage Azure environments, quotas, and compute instances

Gained hands-on experience with model debugging and container crash resolution

Improved understanding of feature engineering, business problem framing, and deployment best practices



---

👨‍💻 Author

Victor Isuo
Microsoft Certified AI/ML Engineer 

📧 Email: victorisuo@gmail.com
🔗 LinkedIn: linkedin.com/in/victor-isuo-a02b6171
💻 GitHub: github.com/Sirvic1321


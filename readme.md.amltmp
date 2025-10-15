Customer Churn Prediction — Version 1 (Deployed on Azure ML)

End-to-End Machine Learning Deployment | Microsoft Azure ML | REST API Endpoint


---

🌍 Project Overview

This project predicts whether a customer is likely to churn (leave the service) based on their demographic and usage data.
It enables companies to identify at-risk customers early and take proactive steps to improve retention and revenue.

The full lifecycle was implemented on Microsoft Azure Machine Learning, from data preprocessing to deployment as a REST API using Managed Online Endpoints.


---

📊 Problem Statement

Customer churn is a major business challenge, especially in the telecommunications industry.
By predicting churn, companies can:

Retain valuable customers,

Personalize offers, and

Reduce marketing costs.


Objective:

> Build and deploy a machine learning model that predicts customer churn and exposes it via an Azure-hosted REST API for real-time predictions.




---

Dataset Description

Source: IBM Telco Customer Churn Dataset

Feature      Description

gender   -    Customer gender (Male/Female)
SeniorCitizen Whether the customer is a senior citizen
Partner, Dependents Family/social status
tenure Duration with the company (months)
PhoneService, InternetService, etc. Customer’s service subscriptions
Contract, PaperlessBilling, PaymentMethod Type of contract & billing method
MonthlyCharges, TotalCharges Payment details
Churn Target variable (Yes = 1, No = 0)


Dataset Size: ~7,000 records
Class Distribution: ~27% churned customers


---

🧮 Model Overview

The model uses a RandomForestClassifier, chosen for its robustness, interpretability, and ability to handle mixed feature types.

🧱 Pipeline Summary

1. Data Cleaning & Feature Encoding


2. Exploratory Data Analysis (EDA)


3. Model Training & Hyperparameter Tuning


4. Evaluation & Metrics Visualization


5. Deployment to Azure ML Endpoint




---

⚙️ Tech Stack & Tools

Category Tools Used

Language Python 3.10
Libraries pandas, scikit-learn, numpy, joblib, json
Cloud Platform Microsoft Azure Machine Learning
Deployment Managed Online Endpoint
Environment Conda YAML configuration
Version Control GitHub



---

📈 Model Evaluation

Metric Value

Accuracy 0.87
Precision 0.82
Recall 0.79
F1 Score 0.80
ROC-AUC 0.91


Visuals:

evaluation/confusion_matrix.png  
evaluation/roc_curve.png

(Insert confusion matrix and ROC curve images above.)


---

🧩 System Architecture

flowchart LR
A[Customer Data] --> B[Data Preprocessing]
B --> C[Model Training]
C --> D[Evaluation & Validation]
D --> E[Azure Model Registry]
E --> F[Azure Online Endpoint]
F --> G[REST API Prediction]


---

🌐 Deployment Details

Attribute Value

Endpoint Name customer-churn-endpoint
Region East US
Compute Type Standard_DS3_v2
Deployment Mode Managed Online Endpoint
Status ✅ Successfully Deployed
Scoring URI <your_endpoint_scoring_uri>



---

🧠 Sample Inference

Input Example:

{
  "data": [[1, 0, 35, 1, 0, 70.35, 1, 2, 3, 4, 5]]
}

Output Example:

{
  "prediction": "Not Churn",
  "probability": 0.06
}


---

⚡ Quick Start

Run locally or reproduce on Azure ML.

# 1. Clone the repository
git clone https://github.com/yourusername/customer-churn-v1.git
cd customer-churn-v1

# 2. Create and activate environment
conda env create -f environment/conda.yaml
conda activate churn-env

# 3. Train the model
python src/train.py

# 4. Deploy model to Azure
python deployment/endpoint_deploy.py

# 5. Test the endpoint
python deployment/test_endpoint.py


---

📦 Project Structure

customer-churn-v1/
│
├── data/
│ └── customer_churn.csv
│
├── src/
│ ├── train.py
│ ├── score.py
│
├── environment/
│ └── conda.yaml
│
├── evaluation/
│ ├── confusion_matrix.png
│ └── roc_curve.png
│
├── deployment/
│ ├── register_model.py
│ ├── endpoint_deploy.py
│ └── test_endpoint.py
│
├── assets/
│ ├── architecture_diagram.png
│ ├── endpoint_screenshot.png
│
└── README.md


---

🔮 Future Improvements (Version 2 Roadmap)

🧩 Explainability

Integrate SHAP Explainability Dashboard to visualize which features drive churn.

> Example: Customers with “Month-to-month” contracts and “Electronic check” payments have higher churn risk.



💻 Streamlit Frontend

Build an interactive Streamlit app for live predictions.

Input customer data dynamically

Display churn prediction and confidence

Visualize feature impacts


⚙️ Automated Retraining

Implement MLOps automation to retrain the model when new data arrives using:

Azure ML pipelines

Automated model versioning

Data drift detection


🗄️ Database Integration

Connect with Azure SQL or Cosmos DB for real-time data ingestion.


---

💡 Key Takeaways

Mastered Azure ML End-to-End workflow — training → deployment → testing

Gained practical experience with debugging containers, quotas, and environments

Built production-level ML assets ready for integration and scaling

Improved understanding of MLOps concepts and model interpretability



---

🙏 Acknowledgements

Microsoft Azure ML Team — for the deployment ecosystem

IBM Telco Dataset — open-source churn dataset

Scikit-learn Community — for robust ML libraries



---

👨‍💻 Author

Victor Island
Machine Learning Engineer | Mechatronics Graduate | AI Enthusiast

📧 Email: [your.email@example.com]
🔗 LinkedIn: [linkedin.com/in/yourprofile]
💻 GitHub: [github.com/yourgithub]


---

📄 License

This project is licensed under the MIT License — see the LICENSE file for details.
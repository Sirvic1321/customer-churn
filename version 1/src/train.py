import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib
import os
from sklearn.metrics import (
    accuracy_score,
    roc_auc_score,
    confusion_matrix,
    classification_report,
    RocCurveDisplay,
    ConfusionMatrixDisplay
    )

# ===============================
# Load and preprocess dataset
# ===============================
data = pd.read_csv("../data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Drop customerID
data = data.drop('customerID', axis=1)

# Convert TotalCharges to numeric
data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')
data['TotalCharges'] = data['TotalCharges'].fillna(data['TotalCharges'].median())

# Encode categorical variables
for column in data.select_dtypes(include='object').columns:
    data[column] = LabelEncoder().fit_transform(data[column])

# ===============================
# Save preprocessed dataset
# ===============================
os.makedirs("../data", exist_ok=True)
data.to_csv("../data/preprocessed_telco_data.csv", index=False)
print("💾 Preprocessed dataset saved to '../data/preprocessed_telco_data.csv'")

# ===============================
# Split data
# ===============================
X = data.drop('Churn', axis=1)
y = data['Churn']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Save train-test splits
train_data = pd.concat([X_train, y_train], axis=1)
test_data = pd.concat([X_test, y_test], axis=1)


# ===============================
# Train model
# ===============================
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]  # for ROC-AUC

# ===============================
# Evaluation metrics
# ===============================
accuracy = accuracy_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_proba)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print("\n📊 Model Evaluation Metrics")
print(f"Accuracy: {accuracy:.3f}")
print(f"ROC-AUC: {roc_auc:.3f}")
print("\nConfusion Matrix:\n", conf_matrix)
print("\nClassification Report:\n", class_report)

# ===============================
# Create folder for plots
# ===============================
os.makedirs("../evaluation", exist_ok=True)

# ===============================
# Plot and save ROC Curve
# ===============================
plt.figure()
RocCurveDisplay.from_predictions(y_test, y_proba)
plt.title("ROC Curve - Customer Churn Model")
plt.savefig("../evaluation/roc_curve.png", dpi=300, bbox_inches='tight')
plt.close()
print("📈 ROC curve saved to '../evaluation/roc_curve.png'")

# ===============================
# Plot and save Confusion Matrix
# ===============================
plt.figure()
ConfusionMatrixDisplay(conf_matrix, display_labels=['No Churn', 'Churn']).plot(cmap='Blues', values_format='d')
plt.title("Confusion Matrix - Customer Churn Model")
plt.savefig("../evaluation/confusion_matrix.png", dpi=300, bbox_inches='tight')
plt.close()
print("Confusion matrix saved to '../evaluation/confusion_matrix.png'")

# ===============================
# Save trained model
# ===============================
os.makedirs("../model", exist_ok=True)
joblib.dump(model, "../model/churn_model.pkl")
print("\n✅ Model trained and saved successfully!")

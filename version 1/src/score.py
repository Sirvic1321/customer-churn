import json
import joblib
import numpy as np
import os

def init():
    global model
    # Path to the registered model in Azure ML
    model_path = os.path.join(os.getenv("AZUREML_MODEL_DIR"), "churn_model.pkl")
    model = joblib.load(model_path)

def run(raw_data):
    try:
        # Parse the incoming JSON data
        data = json.loads(raw_data)["data"]
        input_array = np.array(data)

        # Make predictions
        preds = model.predict(input_array)

        # Get churn probabilities (if classifier supports it)
        if hasattr(model, "predict_proba"):
            probs = model.predict_proba(input_array)[:, 1] # Probability of 'Churn'
        else:
            probs = np.zeros(len(preds)) # fallback

        # Format results
        results = []
        for pred, prob in zip(preds, probs):
            results.append({
                "label": "Churn" if pred == 1 else "Not Churn",
                "probability": round(float(prob), 3)
            })

        # Return JSON response
        return json.dumps({"predictions": results})
    
    except Exception as e:
        return json.dumps({"error": str(e)})
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
from azure.ai.ml.entities import Model

ml_client = MLClient(DefaultAzureCredential(), "<YOUR_SUBSCRIPTION_ID>", "<YOUR_RESOURCE_GROUP>", "<YOUR_WORKSPACE_NAME>")

model = Model(path="../model/churn_model.pkl", name="churn-model", description="Customer churn prediction model")
ml_client.models.create_or_update(model)
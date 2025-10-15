from azure.ai.ml.entities import (
    ManagedOnlineEndpoint,
    ManagedOnlineDeployment,
    Environment,
    CodeConfiguration
)
import datetime

endpoint_name = f"churn-endpoint-{datetime.datetime.now().strftime('%m%d%H%M')}"

# Create endpoint
endpoint = ManagedOnlineEndpoint(
    name=endpoint_name,
    description="Predicts customer churn probability",
    auth_mode="key"
)
ml_client.begin_create_or_update(endpoint).result()

# Create environment
env = Environment(
    name="churn-env",
    conda_file="../environment/conda.yaml",
    image="mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04"
)
# Deployment
deployment = ManagedOnlineDeployment(
    name="blue",
    endpoint_name=endpoint_name,
    model=model,
    environment=env,
    code_configuration=CodeConfiguration(code=".", scoring_script="score.py"),
    instance_type="Standard_DS1_v2",
    instance_count=1
)

ml_client.begin_create_or_update(deployment).result()

# Set traffic
endpoint.traffic = {"blue": 100}
ml_client.begin_create_or_update(endpoint).result()



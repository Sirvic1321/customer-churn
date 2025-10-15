import requests, json

endpoint = ml_client.online_endpoints.get(name=endpoint_name)
scoring_uri = endpoint.scoring_uri
keys = ml_client.online_endpoints.get_keys(name=endpoint_name)
primary_key = keys.primary_key

sample_input = {"data": [[0, 0, 1, 0, 12, 1, 0, 2, 1, 1, 0, 1, 0, 0, 1, 1, 2, 75.5, 1200.25]]}
headers = {"Content-Type": "application/json", "Authorization": f"Bearer {primary_key}"}

response = requests.post(scoring_uri, headers=headers, data=json.dumps(sample_input))
print(response.status_code)
print(response.json())
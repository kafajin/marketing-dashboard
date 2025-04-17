import requests
import json

# Meta Ads API Configuration
API_NAME = "Meta Ads"
API_BASE_URL = "https://graph.facebook.com/v18.0"
ACCESS_TOKEN = "YOUR_META_ACCESS_TOKEN"
AD_ACCOUNT_ID = "act_1234567890"

FIELDS = "name,insights{impressions,clicks,cpc,spend}"

url = f"{API_BASE_URL}/{AD_ACCOUNT_ID}/ads"
params = {
    "fields": FIELDS,
    "access_token": ACCESS_TOKEN
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(f"\n--- {API_NAME} Campaign Data ---")
    print(json.dumps(data, indent=2))
else:
    print("Error:", response.status_code)
    print(response.text)

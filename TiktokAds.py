import requests
import json

API_NAME = "TikTok Ads"
BASE_URL = "https://business-api.tiktok.com/open_api/v1.3"
ACCESS_TOKEN = "YOUR_TIKTOK_ACCESS_TOKEN"
ADVERTISER_ID = "YOUR_ADVERTISER_ID"

url = f"{BASE_URL}/report/ad/get/"
headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

params = {
    "advertiser_id": ADVERTISER_ID,
    "report_type": "BASIC",
    "data_level": "AD",
    "dimensions": ["ad_id", "ad_name"],
    "metrics": ["impressions", "clicks", "spend"],
    "start_date": "2024-03-01",
    "end_date": "2024-03-30"
}

response = requests.post(url, headers=headers, json=params)

if response.status_code == 200:
    data = response.json()
    print(f"\n--- {API_NAME} Campaign Data ---")
    print(json.dumps(data, indent=2))
else:
    print("Error:", response.status_code)
    print(response.text)

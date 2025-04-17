from google.ads.googleads.client import GoogleAdsClient
import json

# Load configuration from google-ads.yaml
client = GoogleAdsClient.load_from_storage("google-ads.yaml")

customer_id = "INSERT_CUSTOMER_ID_HERE"  # Example: "1234567890"

ga_service = client.get_service("GoogleAdsService")

query = """
    SELECT campaign.id, campaign.name, metrics.impressions, metrics.clicks, metrics.cost_micros
    FROM campaign
    WHERE segments.date DURING LAST_30_DAYS
    LIMIT 10
"""

response = ga_service.search(customer_id=customer_id, query=query)

print("--- Google Ads Campaign Data ---")
for row in response:
    print(json.dumps({
        "campaign_id": row.campaign.id,
        "campaign_name": row.campaign.name,
        "impressions": row.metrics.impressions,
        "clicks": row.metrics.clicks,
        "cost_micros": row.metrics.cost_micros
    }, indent=2))

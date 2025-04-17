import pandas as pd
import matplotlib.pyplot as plt

# === Mock campaign data ===
campaigns = [
    {"Campaign": "Winter Sale", "Impressions": 5000, "Clicks": 300, "Cost (SEK)": 150.00, "Revenue (SEK)": 1200},
    {"Campaign": "Spring Launch", "Impressions": 7000, "Clicks": 500, "Cost (SEK)": 250.00, "Revenue (SEK)": 1800},
    {"Campaign": "Summer Deal", "Impressions": 6000, "Clicks": 400, "Cost (SEK)": 200.00, "Revenue (SEK)": 1400},
    {"Campaign": "Autumn Promo", "Impressions": 4000, "Clicks": 240, "Cost (SEK)": 120.00, "Revenue (SEK)": 950},
]

# === Load data ===
df = pd.DataFrame(campaigns)

# === Calculated metrics ===
df["CTR (%)"] = (df["Clicks"] / df["Impressions"]) * 100
df["CPC (SEK)"] = df["Cost (SEK)"] / df["Clicks"]
df["Conversion Rate (%)"] = 10.0  # You can customize this per campaign if you want
df["Conversions"] = (df["Clicks"] * df["Conversion Rate (%)"] / 100).round(0).astype(int)
df["Profit (SEK)"] = df["Revenue (SEK)"] - df["Cost (SEK)"]
df["ROAS"] = (df["Revenue (SEK)"] / df["Cost (SEK)"]).round(2)

# === Print summary table ===
print("\n📊 Extended Campaign Performance:\n")
print(df.to_string(index=False, justify="left", col_space=14))

# === Save to CSV ===
df.to_csv("extended_campaign_analysis.csv", index=False)
print("\n✅ Data exported to 'extended_campaign_analysis.csv'.")

# === Plot: Revenue vs Cost ===
plt.figure(figsize=(8, 5))
bar_width = 0.35
index = range(len(df))

plt.bar(index, df["Revenue (SEK)"], bar_width, label="Revenue", color="green")
plt.bar([i + bar_width for i in index], df["Cost (SEK)"], bar_width, label="Cost", color="red")

plt.xlabel("Campaign")
plt.ylabel("SEK")
plt.title("Revenue vs Cost per Campaign")
plt.xticks([i + bar_width / 2 for i in index], df["Campaign"], rotation=20)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()

import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# === MOCK DATA ===
data = {
    "Campaign": ["Winter Sale", "Spring Launch", "Summer Deal", "Autumn Promo"],
    "Impressions": [5000, 7000, 6000, 4000],
    "Clicks": [300, 500, 400, 240],
    "Cost (SEK)": [150, 250, 200, 120],
    "Revenue (SEK)": [1200, 1800, 1400, 950],
    "Conversion Rate (%)": [8.0, 12.0, 10.0, 9.0],
}

df = pd.DataFrame(data)
df["CTR (%)"] = (df["Clicks"] / df["Impressions"]) * 100
df["CPC (SEK)"] = df["Cost (SEK)"] / df["Clicks"]
df["Conversions"] = (df["Clicks"] * df["Conversion Rate (%)"] / 100).round(0).astype(int)
df["Profit (SEK)"] = df["Revenue (SEK)"] - df["Cost (SEK)"]
df["ROAS"] = df["Revenue (SEK)"] / df["Cost (SEK)"]

# === DASH APP ===
app = dash.Dash(__name__)
app.title = "Marketing Dashboard"

app.layout = html.Div([
    html.H1("📊 Weekly Campaign Dashboard"),

    dcc.Graph(figure=px.bar(df, x="Campaign", y="CTR (%)", title="Click-Through Rate (CTR)")),

    dcc.Graph(figure=px.bar(df, x="Campaign", y="ROAS", title="Return on Ad Spend (ROAS)")),

    dcc.Graph(figure=px.bar(df, x="Campaign", y="Profit (SEK)", title="Profit per Campaign", color="Profit (SEK)")),

    html.Div([
        html.H4("📋 Campaign Table"),
        html.Pre(df.to_string(index=False), style={"whiteSpace": "pre-wrap", "fontFamily": "monospace"})
    ])
])

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8050))
    app.run(host="0.0.0.0", port=port, debug=False)

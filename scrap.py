import requests
import pandas as pd

url = "https://api.takealot.com/rest/v-1-16-0/searches/products,filters,facets,sort_options,breadcrumbs,slots_audience,context,seo,layout"

params = {
    "filter": "ASScreenSize:1016-1092.2",
    "sort": "Relevance",
    "department_slug": "tv-audio-video",
    "category_slug": "tvs-25953",
    "customer_id": "-1442556678",
    "client_id": "31fe46c8-82ae-4488-868a-8d56a5efe7bd"
}

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

resp = requests.get(url, params=params, headers=headers)
resp.raise_for_status()

data = resp.json()

products = data["sections"]["products"]["results"]

rows = []

for item in products:
    pv = item.get("product_views", {})
    core = pv.get("core", {})
    buybox = pv.get("buybox_summary", {})
    review = pv.get("review_summary", {})

    rows.append({
        "title": core.get("title"),
        "brand": core.get("brand"),
        "price": buybox.get("pretty_price"),
        "price_raw": buybox.get("prices", [None])[0],
        "rating": review.get("star_rating"),
        "reviews": review.get("review_count"),
        "product_id": core.get("id"),
    })

df = pd.DataFrame(rows)

df.to_csv("takealot_tvs.csv", index=False, encoding="utf-8-sig")

print(df.head(10))
print("Saved", len(df), "products")
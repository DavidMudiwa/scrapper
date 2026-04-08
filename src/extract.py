import os
import requests
from dotenv import load_dotenv

load_dotenv()  # loads .env file

URL = os.getenv("TAKEALOT_URL")

PARAMS = {
    "filter": os.getenv("FILTER"),
    "sort": os.getenv("SORT"),
    "department_slug": os.getenv("DEPARTMENT"),
    "category_slug": os.getenv("CATEGORY"),
    "customer_id": os.getenv("CUSTOMER_ID"),
    "client_id": os.getenv("CLIENT_ID"),
}

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}


def extract_takealot_data():
    response = requests.get(URL, params=PARAMS, headers=HEADERS, timeout=60)
    response.raise_for_status()
    return response.json()
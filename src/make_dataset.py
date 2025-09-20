import requests 
import pandas as pd

# SQL queries to fetch data
QUERIES = {
    "illegal_dumping_daily": """
        SELECT 
    date_trunc('day', requested_datetime)::date AS day,
    service_code AS srvcCode,
    address AS addr,
    agency_responsible,
    lat,
    lon,
    media_url,
    the_geom,
    cartodb_id,
    requested_datetime,
    expected_datetime,
    closed_datetime
FROM public_cases_fc
WHERE service_code = 'SR-ST02'
AND requested_datetime >= '2016-01-01'
ORDER BY day;
    """
}            

# Function to fetch data from CARTO SQL API
def fetch_data(query: str):
    url = "https://phl.carto.com/api/v2/sql"
    params = {
        "q": query,
        "format": "json"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()["rows"]  # CARTO wraps results in "rows"
    return pd.DataFrame(data)

# Fetch dataset
df = fetch_data(QUERIES["illegal_dumping_daily"])
print(df.head())

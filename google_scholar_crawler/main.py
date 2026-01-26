from serpapi import GoogleSearch
import json
import os
from datetime import datetime

# Get IDs and Keys from environment variables
scholar_id = os.getenv("GOOGLE_SCHOLAR_ID")
serpapi_key = os.getenv("SERPAPI_KEY")

if not scholar_id or not serpapi_key:
    raise EnvironmentError("GOOGLE_SCHOLAR_ID and SERPAPI_KEY are required.")

params = {
    "engine": "google_scholar_author",
    "author_id": scholar_id,
    "api_key": serpapi_key
}

search = GoogleSearch(params)
results = search.get_dict()

# Extract relevant data
author = results.get("author", {})
cited_by = results.get("cited_by", {})

data = {
    "container_type": "Author",
    "filled": ["basics", "indices", "counts"],
    "scholar_id": scholar_id,
    "source": "SERPAPI",
    "name": author.get("name"),
    "affiliation": author.get("affiliations"),
    "citedby": cited_by.get("table", [{}])[0].get("citations", 0),
    "hindex": cited_by.get("table", [{}])[1].get("citations", 0),
    "i10index": cited_by.get("table", [{}])[2].get("citations", 0),
    "cites_per_year": {str(d.get("year")): d.get("citations") for d in cited_by.get("graph", [])},
    "updated": str(datetime.now()),
    "publications": {} # Keep field for compatibility
}

# Save results for shields.io
shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{data['citedby']}",
}

os.makedirs('results', exist_ok=True)
with open('results/gs_data.json', 'w') as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=2)

with open('results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False, indent=2)

print(f"Successfully fetched data for {data['name']}. Total citations: {data['citedby']}")
from apify_client import ApifyClient
import json
from dotenv import load_dotenv
import os

load_dotenv()

client = ApifyClient(os.getenv("APIFY_API_KEY"))

area = input("In which state do you want to search the leads?\n")
query = input("Write the specific industry to get leads for.\n ")

run_input = {
    "area": area,
    "search": query, 
}

run = client.actor("FK0MkqvI0wudAJ1fK").call(run_input=run_input)

items = []
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    items.append(item)

with open("actor_results.json", "w") as f:
    json.dump(items, f, indent=4)

print("Results saved to actor_results.json")

from src.tools import JsonHandler
import pandas as pd
import os
import re


handler = JsonHandler()

datasets = {}


def load_listings_datasets() -> pd.DataFrame:
    for file in os.listdir("data1/all_cities"):
        pattern = r"_(\w{2})"
        match = re.search(pattern, file)
        result = match.group(1)
        datasets[f"df_{result}"] = pd.read_csv(f"data1/all_cities/{file}")
        df = pd.concat([value for key, value in datasets.items()], ignore_index=True)
    return df


df = load_listings_datasets()
host_locations_total = handler.retrieve_host_location(df)
handler.export_to_json(host_locations_total, "data1/mappings/host_locations.json")

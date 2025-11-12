#%%
import pandas as pd
from os import listdir
import json
#%%
dfs = []
for id in listdir("data"):
    with open(f"data/{id}","r") as f:
        data = json.load(f)
        df = pd.DataFrame(data["prices"])
        df["id"] = data["id"]
        dfs.append(df)

#%%
merged = pd.concat(dfs)
merged.columns = ["date", "price", "volume", "id"]
merged["volume"] = pd.to_numeric(merged["volume"])
merged["date"] = pd.to_datetime(merged["date"], format="%b %d %Y %H: +0")
#%%
merged.to_parquet("merged.parquet")
#%%

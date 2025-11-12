#%%
from json import loads,dump
import pandas as pd
from urllib.parse import quote as urlquote
from requests import get
from time import sleep
#%%
items = list(loads(open("cs2-items.json","rb").read()).keys())
#%%
login_token = "76561198304659319%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MDAxNV8yNzM0MkRFMV8yOTREOSIsICJzdWIiOiAiNzY1NjExOTgzMDQ2NTkzMTkiLCAiYXVkIjogWyAid2ViOmNvbW11bml0eSIgXSwgImV4cCI6IDE3NjI5MTM5OTIsICJuYmYiOiAxNzU0MTg2MzM0LCAiaWF0IjogMTc2MjgyNjMzNCwgImp0aSI6ICIwMDExXzI3MzQyRERDX0M2Rjc5IiwgIm9hdCI6IDE3NjI4MjYzMjgsICJydF9leHAiOiAxNzgwNzYxNTA4LCAicGVyIjogMCwgImlwX3N1YmplY3QiOiAiMTI5LjY1LjE0NS4yNTMiLCAiaXBfY29uZmlybWVyIjogIjEyOS42NS4xNDUuMjUzIiB9.z38TYhTZO_CQXPuAlvI3wrDgq3cRLAyR0KdYKxju1oSnHOnd1tur-CJHDPq8aldz7i5NR_Du614YuucBh81XDA; sessionid=681c88839b799b2040f4360b;"
#%%
for i in range(len(items)):
    item_id = items[i]
    print("Querying ",i, item_id)
    res = get(url=f"https://steamcommunity.com/market/pricehistory/?appid=730&market_hash_name={urlquote(item_id)}", cookies={"steamLoginSecure": login_token})

    if res.status_code != 200:
        print(f"Bad Response Code: {res.status_code} on item: {item_id}")
        break
    data = res.json()
    data["id"] = item_id
    with open(f"./data/{i}.json", "w") as f:
        dump(fp=f,obj=data)
        f.close()
        print("saved")
    sleep(0.5)
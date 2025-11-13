# Gather Data + EDA for Final Project
Curtis Bradley & Connor Villanueva

## Dataset Selection
Our dataset is Steam Community Market Data from CSGO/CS2. We chose this dataset because we were originally interested in predicting market trends and seeing how different models perform with this task. 

However, after discussing with Pierce, we decided to switch our topic slightly. Now we are interested in seeing if we can predict winning teams/top players from tournmanets by viewing market data during a window of time from before the tournament until after. 

This dataset was obtained by sending HTTP requests to the following URL: `https://steamcommunity.com/market/pricehistory/?appid=730&market_hash_name={ITEM}` where `ITEM` is the name of CSGO/CS2 item that has been url encoded. This data was then combined with results from an unofficial JSON API, `https://raw.githubusercontent.com/ByMykel/CSGO-API/main/public/api/el/`, that we found at the following link with instructions: `https://bymykel.com/CSGO-API/#introduction`

The official Steam Community Market provides the median price and volume sold in the following way:

- Hourly for data within the last month
- Daily for data that is over a month old


## Exploratory Data Analysis (EDA)

![image](./images/freq_dist_stickers.png)


## Issues/Questions
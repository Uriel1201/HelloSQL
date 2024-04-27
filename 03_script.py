# %%
# !! {"metadata":{
# !!   "id": "6QyBJJSnBzKL"
# !! }}
"""
# 03. Most Frequent Items
From the following table containing a list of dates and items ordered, write a query to return the most frequent item ordered on each date. Return multiple items in the case of a tie.
"""

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 300
# !!   },
# !!   "id": "ZmvZS5T5CTdN",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714181665122,
# !!     "user_tz": 360,
# !!     "elapsed": 188,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "bb3003bf-e7d9-4021-b317-b6f6890864a6"
# !! }}
import pandas as pd
import numpy as  np

data = {'dates' : ['01-JAN-20',
                   '01-JAN-20',
                   '01-JAN-20',
                   '01-JAN-20',
                   '02-JAN-20',
                   '02-JAN-20',
                   '02-JAN-20',
                   '02-JAN-20'],
        'item' : ['apple',
                  'apple',
                  'pear',
                  'pear',
                  'pear',
                  'pear',
                  'pear',
                  'orange']

       }
items = pd.DataFrame(data)
items

# %%
# !! {"metadata":{
# !!   "id": "l1CALdHMDTRT",
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 355
# !!   },
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714181671051,
# !!     "user_tz": 360,
# !!     "elapsed": 228,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "f4bdbb27-f97c-44af-f3f3-818ac65563d7"
# !! }}
items['dates'] = pd.to_datetime(items['dates'])
items

# %%
# !! {"metadata":{
# !!   "id": "YrFCwMoOHwGc",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714181679151,
# !!     "user_tz": 360,
# !!     "elapsed": 184,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
item_counts = items.groupby(['dates', 'item']).size().reset_index(name = 'counts')

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 174
# !!   },
# !!   "id": "Zw-xTDVaILQi",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714181711590,
# !!     "user_tz": 360,
# !!     "elapsed": 224,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "7ed8a5bb-124f-47c4-96fb-8dd24e5b886a"
# !! }}
item_counts

# %%
# !! {"metadata":{
# !!   "id": "dckh8xUyJzXp",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714181720265,
# !!     "user_tz": 360,
# !!     "elapsed": 170,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
item_counts['item_rank'] = item_counts.groupby('dates')['counts'].rank(method = 'dense', ascending = False)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 264
# !!   },
# !!   "id": "2rVXYVj6KVkH",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714181753284,
# !!     "user_tz": 360,
# !!     "elapsed": 222,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "6f6cee06-fb04-4451-e381-a2a0958f51d1"
# !! }}
item_counts

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 143
# !!   },
# !!   "id": "-QLBhu0nKdJu",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714181812349,
# !!     "user_tz": 360,
# !!     "elapsed": 175,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "2029d2cb-003a-4800-b2bb-9665f2974299"
# !! }}
item_counts[['dates', 'item']][item_counts['item_rank'] == 1.0]

# %%
# !! {"main_metadata":{
# !!   "colab": {
# !!     "provenance": [],
# !!     "authorship_tag": "ABX9TyOrd4lmTw17nC+Mf/CiwJBx"
# !!   },
# !!   "kernelspec": {
# !!     "name": "python3",
# !!     "display_name": "Python 3"
# !!   },
# !!   "language_info": {
# !!     "name": "python"
# !!   }
# !! }}

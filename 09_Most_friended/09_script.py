# %%
# !! {"metadata":{
# !!   "id": "BCt9pp-f5TA5"
# !! }}
"""
# 9. Most friended
Given the following table, return a list of users and their corresponding friend count. Order the result by descending friend count, and in the case of a tie, by ascending user ID. Assume that only unique friendships are displayed
"""

# %%
# !! {"metadata":{
# !!   "id": "WLjR3J435TUQ"
# !! }}
import pandas as pd
import numpy  as np

data    = {'user_1' : [1,1,1,2],
           'user_2' : [2,3,4,3]
          }
friends = pd.DataFrame(data)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 174
# !!   },
# !!   "id": "iVKpgLbI5jdO",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715136689920,
# !!     "user_tz": 360,
# !!     "elapsed": 171,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "ff04e9f1-8421-43e4-f232-7d8be7872f44"
# !! }}
friends

# %%
# !! {"metadata":{
# !!   "id": "rl5bMwgk6GFN",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715136692888,
# !!     "user_tz": 360,
# !!     "elapsed": 139,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
friend_counts = pd.DataFrame(pd.concat([friends['user_1'], friends['user_2']]))

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 300
# !!   },
# !!   "id": "Ahv8THH0GBhl",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715136694906,
# !!     "user_tz": 360,
# !!     "elapsed": 157,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "9669bf4a-3d20-44d6-a649-c2582009e631"
# !! }}
friend_counts

# %%
# !! {"metadata":{
# !!   "id": "klLFVLTw67Vn",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715136700969,
# !!     "user_tz": 360,
# !!     "elapsed": 129,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
friend_counts = pd.DataFrame(friend_counts.groupby(0).size())

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 206
# !!   },
# !!   "id": "-H1DlptVGLSW",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715136702790,
# !!     "user_tz": 360,
# !!     "elapsed": 208,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "576a60e2-7372-4b05-a30e-36a8417b8970"
# !! }}
friend_counts

# %%
# !! {"metadata":{
# !!   "id": "qzDKCh4NFDV7",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715136839811,
# !!     "user_tz": 360,
# !!     "elapsed": 145,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
friend_counts.rename(columns = {0 : 'number_friends'}, inplace = True)
friend_counts.reset_index(inplace = True)
friend_counts.rename(columns = {0 : 'user_id'}, inplace = True)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 174
# !!   },
# !!   "id": "WkfcLdQDHEA3",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715137150206,
# !!     "user_tz": 360,
# !!     "elapsed": 150,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "a2887697-f913-4759-d287-1801cab0c47c"
# !! }}
friend_counts

# %%
# !! {"main_metadata":{
# !!   "colab": {
# !!     "provenance": [],
# !!     "authorship_tag": "ABX9TyOv44z0Yi3txzY8pHXyBT9k"
# !!   },
# !!   "kernelspec": {
# !!     "name": "python3",
# !!     "display_name": "Python 3"
# !!   },
# !!   "language_info": {
# !!     "name": "python"
# !!   }
# !! }}

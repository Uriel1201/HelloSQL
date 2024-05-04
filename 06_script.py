# %%
# !! {"metadata":{
# !!   "id": "35vL8s5p0GNq"
# !! }}
"""
#06. Content recommendation (hard)
Using the following two tables, write a query to return page recommendations to a social media user based on the pages that their friends have liked, but that they have not yet marked as liked. Order the result by ascending user ID.
"""

# %%
# !! {"metadata":{
# !!   "id": "Wd_UIIVb0GaH",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714758039248,
# !!     "user_tz": 360,
# !!     "elapsed": 637,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
import pandas as pd
import numpy  as np

data1 = {'user_id': [1,1,1,2,3,3,4,4],
         'friend'  : [2,3,4,1,1,4,1,3]
        }

data2 = {'user_id' : [1,1,1,2,3,3,4],
         'page_likes' : ['A','B','C','A','B','C','B']
        }

friends = pd.DataFrame(data1)
likes   = pd.DataFrame(data2)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 300
# !!   },
# !!   "executionInfo": {
# !!     "elapsed": 211,
# !!     "status": "ok",
# !!     "timestamp": 1714758042554,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     },
# !!     "user_tz": 360
# !!   },
# !!   "id": "F_gkVy670_5K",
# !!   "outputId": "2f568507-ba6e-4a6b-f0c9-1d626e2bf03f"
# !! }}
friends

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 269
# !!   },
# !!   "executionInfo": {
# !!     "elapsed": 279,
# !!     "status": "ok",
# !!     "timestamp": 1714758046434,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     },
# !!     "user_tz": 360
# !!   },
# !!   "id": "C8j-6TxQ1Bu_",
# !!   "outputId": "4ceb694a-a39c-48bb-baea-e692e25953b0"
# !! }}
likes

# %%
# !! {"metadata":{
# !!   "id": "aVZwf0M61owQ",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714758053974,
# !!     "user_tz": 360,
# !!     "elapsed": 413,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
friends_likes = pd.merge(friends, likes, left_on = 'friend', right_on = 'user_id')

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 571
# !!   },
# !!   "executionInfo": {
# !!     "elapsed": 554,
# !!     "status": "ok",
# !!     "timestamp": 1714758056968,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     },
# !!     "user_tz": 360
# !!   },
# !!   "id": "zRfIx2sD3HGN",
# !!   "outputId": "e129e780-528f-47f3-9da7-53025f532507"
# !! }}
friends_likes

# %%
# !! {"metadata":{
# !!   "id": "TXjUmMfR3Y7m",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714758062627,
# !!     "user_tz": 360,
# !!     "elapsed": 181,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
friends_likes.drop('user_id_y', axis = 1, inplace = True)
friends_likes.rename(columns = {'user_id_x' : 'user_id', 'page_likes' : 'friend_page_likes'}, inplace = True)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 571
# !!   },
# !!   "executionInfo": {
# !!     "elapsed": 182,
# !!     "status": "ok",
# !!     "timestamp": 1714758064545,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     },
# !!     "user_tz": 360
# !!   },
# !!   "id": "GtbJ0Eup36yk",
# !!   "outputId": "ee41d6c2-6f3e-4d24-9dc8-3bc3692d2604"
# !! }}
friends_likes

# %%
# !! {"metadata":{
# !!   "id": "mpmeeAIPPmPc",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714758085234,
# !!     "user_tz": 360,
# !!     "elapsed": 218,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
friends_likes.set_index(['user_id', 'friend_page_likes'], inplace = True, drop = False)
user_likes = likes.set_index(['user_id', 'page_likes'], drop = False)

# %%
# !! {"metadata":{
# !!   "id": "VVD7gsC1Rz6k",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714758090140,
# !!     "user_tz": 360,
# !!     "elapsed": 169,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
friends_likes.rename_axis(index = {'friend_page_likes' : 'page_likes'}, inplace = True)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 602
# !!   },
# !!   "executionInfo": {
# !!     "elapsed": 168,
# !!     "status": "ok",
# !!     "timestamp": 1714758093003,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     },
# !!     "user_tz": 360
# !!   },
# !!   "id": "l6Nox0cWTo0e",
# !!   "outputId": "4eb34ee8-2ff3-4aec-c608-147d53a65b2e"
# !! }}
friends_likes

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 320
# !!   },
# !!   "executionInfo": {
# !!     "elapsed": 149,
# !!     "status": "ok",
# !!     "timestamp": 1714758100196,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     },
# !!     "user_tz": 360
# !!   },
# !!   "id": "KRKsZa01odYV",
# !!   "outputId": "5349efcc-7ff9-42b5-81ab-6f9275617265"
# !! }}
user_likes

# %%
# !! {"metadata":{
# !!   "id": "FTYrA02uQifN",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714758105939,
# !!     "user_tz": 360,
# !!     "elapsed": 161,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
user_likes.drop('user_id', axis = 1, inplace = True)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 320
# !!   },
# !!   "id": "M2XOTqaOQx5c",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714758108192,
# !!     "user_tz": 360,
# !!     "elapsed": 167,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "c28e8a8b-22a1-452a-f8ba-d599d87a9019"
# !! }}
user_likes

# %%
# !! {"metadata":{
# !!   "id": "92OXH0Thohaz",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714758122729,
# !!     "user_tz": 360,
# !!     "elapsed": 142,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
is_liked = pd.concat([friends_likes, user_likes], axis = 1, join = 'outer')

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 602
# !!   },
# !!   "id": "OuzAAtM5Rq5w",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714758124622,
# !!     "user_tz": 360,
# !!     "elapsed": 199,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "0147350e-fbdd-4c67-af61-7e6eeaba60e5"
# !! }}
is_liked

# %%
# !! {"metadata":{
# !!   "id": "sEqdlPkmSj5E",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714758144719,
# !!     "user_tz": 360,
# !!     "elapsed": 158,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
recomendations = is_liked[['user_id']][is_liked['page_likes'].isnull()]

# %%
# !! {"metadata":{
# !!   "id": "jfo5GDrRTvLm",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714758155216,
# !!     "user_tz": 360,
# !!     "elapsed": 140,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
recomendations.drop('user_id', axis = 1,inplace = True)
recomendations.reset_index(inplace = True)

# %%
# !! {"metadata":{
# !!   "id": "hqjI18BRXON1",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714758160259,
# !!     "user_tz": 360,
# !!     "elapsed": 152,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
recomendations.rename(columns = {'page_likes' : 'recommended_page'}, inplace = True)
recomendations.drop_duplicates(inplace = True)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 206
# !!   },
# !!   "id": "4fWj0T0HXEyc",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714758162453,
# !!     "user_tz": 360,
# !!     "elapsed": 162,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "4b827529-bb3a-47f8-cd63-1391529918f9"
# !! }}
recomendations.sort_values(by = 'user_id')

# %%
# !! {"main_metadata":{
# !!   "colab": {
# !!     "provenance": [],
# !!     "authorship_tag": "ABX9TyP92scI/gKQTxs4MhzrdQKl"
# !!   },
# !!   "kernelspec": {
# !!     "display_name": "Python 3",
# !!     "name": "python3"
# !!   },
# !!   "language_info": {
# !!     "name": "python"
# !!   }
# !! }}

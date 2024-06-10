# %%
# !! {"metadata":{
# !!   "id": "KgFBDBji1231"
# !! }}
"""
# 15. Team standings
Write a query to return the scores of
each team in the teams table after all
matches displayed in the matches table.
Points are awarded as follows: zero
points for a loss, one point for a tie, and
three points for a win. The result should
include team name and points, and be
ordered by decreasing points.
"""

# %%
# !! {"metadata":{
# !!   "id": "_GuODcby13HN",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1717993126355,
# !!     "user_tz": 360,
# !!     "elapsed": 8,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
import pandas as pd
import numpy  as np

data1 = {'team_id' : [1,2,3,4,5,6],
         'team_name' : ['New York','Atlanta','Chicago','Toronto','Los Angeles','Seattle']
        }

data2 = {'match_id'    : [1,2,3,4,5,6],
         'host_team'   : [1,2,3,4,5,6],
         'guest_team'  : [2,3,4,5,6,1],
         'host_goals'  : [3,2,4,1,2,1],
         'guest_goals' : [0,4,3,1,1,2]
        }

teams   = pd.DataFrame(data1)
matches = pd.DataFrame(data2)

# %%
# !! {"metadata":{
# !!   "id": "nbL7tFxZ2CFc",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1717993129665,
# !!     "user_tz": 360,
# !!     "elapsed": 203,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "17ce6822-0a3e-47dd-a0c7-b3b90f4b5748",
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 238
# !!   }
# !! }}
teams

# %%
# !! {"metadata":{
# !!   "id": "C4YHsfqXao4g",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1717994242494,
# !!     "user_tz": 360,
# !!     "elapsed": 207,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
teams.set_index('team_id', inplace = True)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 269
# !!   },
# !!   "id": "a0brP9VKdjmv",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1717994674175,
# !!     "user_tz": 360,
# !!     "elapsed": 385,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "5c4d1ec5-0e11-4c1b-ec5f-3f7811a66e69"
# !! }}
teams

# %%
# !! {"metadata":{
# !!   "id": "U-UHPAd52DzR",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1717993133115,
# !!     "user_tz": 360,
# !!     "elapsed": 244,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "902ae19b-1221-44e5-e193-b6671a3a9f67",
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 258
# !!   }
# !! }}
matches

# %%
# !! {"metadata":{
# !!   "id": "ZZ9V_oIlCDjQ",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1717993175699,
# !!     "user_tz": 360,
# !!     "elapsed": 213,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
host_matches = matches[['host_team', 'host_goals', 'guest_goals']].copy()
host_matches.rename(columns = {'host_team' : 'team_id'}, inplace = True)
host_matches['host_scores'] = np.where(host_matches['host_goals'] > host_matches['guest_goals'], 3 ,np.where(host_matches['host_goals'] == host_matches['guest_goals'], 1, 0))

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 258
# !!   },
# !!   "id": "OcGXs_xNOG3K",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1717993178156,
# !!     "user_tz": 360,
# !!     "elapsed": 229,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "616ac621-84e4-4cf4-8205-a9f535662072"
# !! }}
host_matches

# %%
# !! {"metadata":{
# !!   "id": "8bCGi9CyX5B7",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1717993303811,
# !!     "user_tz": 360,
# !!     "elapsed": 156,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
host_scores = pd.DataFrame(host_matches.groupby('team_id')['host_scores'].sum())

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 269
# !!   },
# !!   "id": "W9krKrOlYXd7",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1717993313813,
# !!     "user_tz": 360,
# !!     "elapsed": 208,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "6a4d8b34-6a23-4a72-810a-f8d08281b1f8"
# !! }}
host_scores

# %%
# !! {"metadata":{
# !!   "id": "367IidEEPC6B",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1717993330123,
# !!     "user_tz": 360,
# !!     "elapsed": 155,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
guest_matches = matches[['guest_team', 'host_goals', 'guest_goals']].copy()
guest_matches.rename(columns = {'guest_team' : 'team_id'}, inplace = True)
guest_matches['guest_scores'] = np.where(guest_matches['guest_goals'] > guest_matches['host_goals'], 3 ,np.where(guest_matches['guest_goals'] == guest_matches['host_goals'], 1, 0))

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 258
# !!   },
# !!   "id": "tFKKA4jkQV3X",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1717993333259,
# !!     "user_tz": 360,
# !!     "elapsed": 212,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "a82d5640-1594-46cc-be46-25e7871f5ed0"
# !! }}
guest_matches

# %%
# !! {"metadata":{
# !!   "id": "1UE4e84UYiox",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1717993455915,
# !!     "user_tz": 360,
# !!     "elapsed": 156,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
guest_scores = pd.DataFrame(guest_matches.groupby('team_id')['guest_scores'].sum())

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 269
# !!   },
# !!   "id": "zmfX-n1sY8jl",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1717993466571,
# !!     "user_tz": 360,
# !!     "elapsed": 188,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "6e48628d-48fb-4a96-a6bc-12a11a24ea4f"
# !! }}
guest_scores

# %%
# !! {"metadata":{
# !!   "id": "WNEuAVYnZCjP",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1717994807296,
# !!     "user_tz": 360,
# !!     "elapsed": 191,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
scores = pd.concat([host_scores, guest_scores], axis = 1, join = 'inner')

# %%
# !! {"metadata":{
# !!   "id": "UhKMRfoeZqmi",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1717994809230,
# !!     "user_tz": 360,
# !!     "elapsed": 170,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
scores = pd.DataFrame(scores['host_scores'] + scores['guest_scores'])
scores.rename(columns = {0 : 'score'}, inplace = True)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 269
# !!   },
# !!   "id": "6NihBDhlaM3Q",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1717993876754,
# !!     "user_tz": 360,
# !!     "elapsed": 157,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "dee0b55b-755e-42ba-a065-82ff88d2bcc4"
# !! }}
scores

# %%
# !! {"metadata":{
# !!   "id": "yDgpng_4b-oj",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1717994381126,
# !!     "user_tz": 360,
# !!     "elapsed": 191,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
results = pd.concat([teams, scores], axis = 1, join = 'inner')

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 269
# !!   },
# !!   "id": "oMXFAiIDceR-",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1717994452992,
# !!     "user_tz": 360,
# !!     "elapsed": 230,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "d8e89034-9643-4296-cb6e-0d385dda884b"
# !! }}
results.sort_values(by = 'score', ascending = False)

# %%
# !! {"main_metadata":{
# !!   "colab": {
# !!     "provenance": [],
# !!     "authorship_tag": "ABX9TyOlIowglse07zFuyiC5oK3N"
# !!   },
# !!   "kernelspec": {
# !!     "name": "python3",
# !!     "display_name": "Python 3"
# !!   },
# !!   "language_info": {
# !!     "name": "python"
# !!   }
# !! }}

# %%
# !! {"metadata":{
# !!   "id": "wT7yQLFI5JTC"
# !! }}
"""
# 7. Mobile and web visitors
With the following two tables, return the fraction of users who only visited mobile,only visited web, and visited both.
"""

# %%
# !! {"metadata":{
# !!   "id": "T44Vp4Hz5JjE",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714976629200,
# !!     "user_tz": 360,
# !!     "elapsed": 854,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
import pandas as pd
import numpy  as np

data1 = {'user_id'   : [1,2,3,4,9,2,10],
         'page_url'  : ['A','B','C','A','B','C','B']
        }

data2 = {'user_id'    : [6,2,3,7,4,8,5],
         'page_url'   : ['A','B','C','A','B','C','B']
        }

mobile = pd.DataFrame(data1)
web    = pd.DataFrame(data2)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 269
# !!   },
# !!   "executionInfo": {
# !!     "elapsed": 162,
# !!     "status": "ok",
# !!     "timestamp": 1714976632632,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     },
# !!     "user_tz": 360
# !!   },
# !!   "id": "nXBYpqsRQhJ-",
# !!   "outputId": "f3943efd-844e-4793-fe4d-eaa5b5283a47"
# !! }}
mobile

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 269
# !!   },
# !!   "executionInfo": {
# !!     "elapsed": 142,
# !!     "status": "ok",
# !!     "timestamp": 1714976635906,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     },
# !!     "user_tz": 360
# !!   },
# !!   "id": "TSYYtX5VQi3_",
# !!   "outputId": "4add8286-005f-4f5f-ddeb-41935627d30a"
# !! }}
web

# %%
# !! {"metadata":{
# !!   "id": "buTLkCVzXQ_j",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714976671418,
# !!     "user_tz": 360,
# !!     "elapsed": 151,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
mobile_users = pd.DataFrame(mobile['user_id'].drop_duplicates())
web_users = pd.DataFrame(web['user_id'].drop_duplicates())
mobile_users['mobile_user'] = mobile_users['user_id']
web_users['web_user'] = web_users['user_id']

# %%
# !! {"metadata":{
# !!   "id": "of0BDjXgWQB1",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714976673856,
# !!     "user_tz": 360,
# !!     "elapsed": 142,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
mobile_users.set_index('user_id', inplace = True)
web_users.set_index('user_id', inplace = True)

# %%
# !! {"metadata":{
# !!   "id": "Uu0ESQ3VQpqz",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714976701509,
# !!     "user_tz": 360,
# !!     "elapsed": 141,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
matches = pd.concat([mobile_users, web_users], axis = 1, join = 'outer')

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 414
# !!   },
# !!   "executionInfo": {
# !!     "elapsed": 215,
# !!     "status": "ok",
# !!     "timestamp": 1714976704615,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     },
# !!     "user_tz": 360
# !!   },
# !!   "id": "XzOF90UASIvC",
# !!   "outputId": "2f2757bf-6d92-451c-8f8b-09c379eedfa7"
# !! }}
matches

# %%
# !! {"metadata":{
# !!   "id": "mgP7J-fBMHbD",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714976808606,
# !!     "user_tz": 360,
# !!     "elapsed": 142,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
matches['only_mobile'] = np.where(np.logical_and(~np.isnan(matches['mobile_user']), np.isnan(matches['web_user'])), True, False)
matches['only_web'] = np.where(np.logical_and(~np.isnan(matches['web_user']), np.isnan(matches['mobile_user'])), True, False)
matches['both'] = np.where(np.logical_and(~np.isnan(matches['mobile_user']), ~np.isnan(matches['web_user'])), True, False)

# %%
# !! {"metadata":{
# !!   "id": "oWNjOdxxgUtT",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714976818757,
# !!     "user_tz": 360,
# !!     "elapsed": 142,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
matches = matches[['only_mobile', 'only_web', 'both']]

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 414
# !!   },
# !!   "id": "qBRvHDDngidN",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714976821291,
# !!     "user_tz": 360,
# !!     "elapsed": 151,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "05d527d0-8ec1-4df3-bcb2-b45b04cba3d7"
# !! }}
matches

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 143
# !!   },
# !!   "id": "AlDenB72hjsM",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714976832763,
# !!     "user_tz": 360,
# !!     "elapsed": 136,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "faae091b-5d73-40d4-9959-9987d607bada"
# !! }}
pd.DataFrame(matches.mean())

# %%
# !! {"main_metadata":{
# !!   "colab": {
# !!     "provenance": [],
# !!     "authorship_tag": "ABX9TyNVPKKmGW12m9fUOSO3jH6i"
# !!   },
# !!   "kernelspec": {
# !!     "display_name": "Python 3",
# !!     "name": "python3"
# !!   },
# !!   "language_info": {
# !!     "name": "python"
# !!   }
# !! }}

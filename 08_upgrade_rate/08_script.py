# %%
# !! {"metadata":{
# !!   "id": "6nnvoOad0nlK"
# !! }}
"""
# 8. Upgrade rate by product action (hard)
Given the following two tables, return the fraction of users, rounded to two decimal places, who accessed feature two (type: F2 in events table) and upgraded to premium within the first 30 days of signing up.
"""

# %%
# !! {"metadata":{
# !!   "id": "Zt8_BEDH1hmV",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715130350456,
# !!     "user_tz": 360,
# !!     "elapsed": 12,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
import pandas as pd
import numpy  as np

data1 = {'user_id'   : [1,2,3,4,5,6,7],
         'name'      : ['John','Jane','Jill','Josh','Jean','Justin','Jeremy'],
         'join_date' : ['14-feb-20',
                        '14-feb-20',
                        '15-feb-20',
                        '15-feb-20',
                        '16-feb-20',
                        '17-feb-20',
                        '18-feb-20']
        }

data2 = {'user_id'     : [1,2,2,3,4,1,3],
         'Type'        : ['F1','F2','P','F2','F2','P','P'],
         'access_date' : ['1-mar-20',
                          '2-mar-20',
                          '12-mar-20',
                          '15-mar-20',
                          '15-mar-20',
                          '16-mar-20',
                          '22-mar-20']
        }

users  = pd.DataFrame(data1)
events = pd.DataFrame(data2)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/"
# !!   },
# !!   "id": "o1tbk5Og2-VW",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715130353777,
# !!     "user_tz": 360,
# !!     "elapsed": 168,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "0693d12a-a16a-4254-9887-fe5e5f7b90bd"
# !! }}
users['join_date'] = pd.to_datetime(users['join_date'])
events['access_date'] = pd.to_datetime(events['access_date'])

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 269
# !!   },
# !!   "id": "pIqCrIlN2rIY",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715130357000,
# !!     "user_tz": 360,
# !!     "elapsed": 158,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "b41ed688-db58-4e1c-8bee-8a60f22d77d6"
# !! }}
users

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 269
# !!   },
# !!   "id": "ZANo9OiK2s9x",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715130359752,
# !!     "user_tz": 360,
# !!     "elapsed": 141,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "766c296a-630a-4073-fda3-d2eb01f644df"
# !! }}
events

# %%
# !! {"metadata":{
# !!   "id": "k9FdwfNOVDyp",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715130364779,
# !!     "user_tz": 360,
# !!     "elapsed": 153,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
def row_num(x):
      x_s = pd.Series(x)
      row_n = range(1, len(x_s) + 1)
      return row_n

# %%
# !! {"metadata":{
# !!   "id": "oH0vBJjA2H_v",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715130367931,
# !!     "user_tz": 360,
# !!     "elapsed": 148,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
events['access_rank'] = events.groupby('user_id')['access_date'].transform(row_num)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 289
# !!   },
# !!   "id": "z9ORaWfq5v78",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715130369967,
# !!     "user_tz": 360,
# !!     "elapsed": 142,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "5b1815e2-6684-4485-8ce0-2c17bc645e93"
# !! }}
events

# %%
# !! {"metadata":{
# !!   "id": "0w1ni5VTRc3q",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715130377267,
# !!     "user_tz": 360,
# !!     "elapsed": 182,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
c1 = events['Type'] == 'F2'
c2 = events['access_rank'] == 1
first_F2 = events.loc[c1 & c2, ['user_id', 'access_date']]

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 143
# !!   },
# !!   "id": "vjBrQqEoSexP",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715130381654,
# !!     "user_tz": 360,
# !!     "elapsed": 205,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "07b499b8-d8d0-4177-fdd9-a0acc37a0a9e"
# !! }}
first_F2

# %%
# !! {"metadata":{
# !!   "id": "RuxgJsgxWOvb",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715130388378,
# !!     "user_tz": 360,
# !!     "elapsed": 148,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
first_F2.set_index('user_id', inplace = True)
users.set_index('user_id', inplace = True)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 174
# !!   },
# !!   "id": "62vtUhm5l0jA",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715130391011,
# !!     "user_tz": 360,
# !!     "elapsed": 451,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "7b95af5b-79ef-4a6d-ba36-f523cff38848"
# !! }}
first_F2

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 300
# !!   },
# !!   "id": "LuEzmuzTl3Cv",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715130399946,
# !!     "user_tz": 360,
# !!     "elapsed": 419,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "538541dc-919e-4e6e-8e7a-9c8558073dee"
# !! }}
users

# %%
# !! {"metadata":{
# !!   "id": "OzL51i21lRwl",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715130415056,
# !!     "user_tz": 360,
# !!     "elapsed": 146,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
c = events['Type'] == 'P'
premium_users = events.loc[c, ['user_id', 'access_date']]

# %%
# !! {"metadata":{
# !!   "id": "aGJKtPBlmYj3",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715130419857,
# !!     "user_tz": 360,
# !!     "elapsed": 166,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
premium_users.set_index('user_id', inplace = True)
premium_users.rename(columns = {'access_date' : 'access_premium_date'}, inplace = True)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 174
# !!   },
# !!   "id": "t4VqYiWtmkAf",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715130442506,
# !!     "user_tz": 360,
# !!     "elapsed": 131,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "b1ad0ebe-666b-49d1-8571-4433d91db237"
# !! }}
premium_users

# %%
# !! {"metadata":{
# !!   "id": "9hVeDB5Wkobv",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715130459609,
# !!     "user_tz": 360,
# !!     "elapsed": 220,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
F2_users = pd.concat([users, first_F2], axis = 1, join = 'inner')

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 194
# !!   },
# !!   "id": "dNouT5iRnHNS",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715130461792,
# !!     "user_tz": 360,
# !!     "elapsed": 161,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "677e7827-98ef-4877-ff83-4bc54885de61"
# !! }}
F2_users

# %%
# !! {"metadata":{
# !!   "id": "XtZtE802nt8j",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715130575219,
# !!     "user_tz": 360,
# !!     "elapsed": 139,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
F2_toP = pd.merge(F2_users, premium_users, left_index = True, right_index = True, how = 'left')

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 194
# !!   },
# !!   "id": "ATm47BNXoBWv",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715130577284,
# !!     "user_tz": 360,
# !!     "elapsed": 134,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "5e3ab313-b6f9-48b8-fcc7-05de1905017c"
# !! }}
F2_toP

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 89
# !!   },
# !!   "id": "ymftkoeBsVFQ",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715130636180,
# !!     "user_tz": 360,
# !!     "elapsed": 139,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "8633c4fd-cf36-45fe-cd87-5d8dd1edb1ac"
# !! }}
i = (np.where(F2_toP['access_premium_date'] - F2_toP['join_date'] <= pd.to_timedelta('30 days'), 1, 0).sum() / len(F2_toP.index)).round(2)
d = {'upgrade_rate' : [i]
    }
upgrade = pd.DataFrame(data = d, index = [0])
upgrade

# %%
# !! {"main_metadata":{
# !!   "colab": {
# !!     "provenance": [],
# !!     "authorship_tag": "ABX9TyMeClcSLGjPD3SX1yLiR+Fz"
# !!   },
# !!   "kernelspec": {
# !!     "name": "python3",
# !!     "display_name": "Python 3"
# !!   },
# !!   "language_info": {
# !!     "name": "python"
# !!   }
# !! }}

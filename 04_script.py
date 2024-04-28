# %%
# !! {"metadata":{
# !!   "id": "MPBfU8MYM4UW"
# !! }}
"""
# 04. Time difference between latest actions.
From the following table of user actions, write a query to return for each user the time elapsed between the last action and the second-to-last action, in ascending order by user ID.
"""

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 320
# !!   },
# !!   "id": "7S872Cm-M5nB",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714272288573,
# !!     "user_tz": 360,
# !!     "elapsed": 801,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "bc8ed431-1a5c-4f6e-b654-325056d6ec0c"
# !! }}
import pandas as pd
import numpy as  np

data = {'user_id' : [1,1,2,2,3,3,4,1],
        'actions'    : ['start','cancel','start',
                    'publish','start','cancel',
                    'start','publish'],
        'action_date'   : ['12-FEB-20',
                         '13-FEB-20',
                         '11-FEB-20',
                         '14-FEB-20',
                         '15-FEB-20',
                         '15-FEB-20',
                         '18-FEB-20',
                         '19-FEB-20']
        }

users = pd.DataFrame(data)
users

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/"
# !!   },
# !!   "id": "PIwyPf4ONtVK",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714272296398,
# !!     "user_tz": 360,
# !!     "elapsed": 162,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "33017393-b714-479d-88dc-98264d6ec938"
# !! }}
users['action_date'] = pd.to_datetime(users['action_date'])

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 320
# !!   },
# !!   "id": "VHdEU9PcOCSL",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714272299377,
# !!     "user_tz": 360,
# !!     "elapsed": 147,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "8909b07c-2a76-49bf-e8c7-7ec168b63a8e"
# !! }}
users

# %%
# !! {"metadata":{
# !!   "id": "2fc7LvuOdyLu"
# !! }}
def row_num(x):
    x_s = pd.Series(x)
    row_n = range(len(x), 0, -1)
    return row_n

# %%
# !! {"metadata":{
# !!   "id": "6JHN_rx6ey_s"
# !! }}
users['date_rank'] = users.groupby('user_id')['action_date'].transform(row_num)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 320
# !!   },
# !!   "id": "RZT69YJDfzr-",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714272311299,
# !!     "user_tz": 360,
# !!     "elapsed": 164,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "9c44dad8-ca4a-4314-b8d6-b43f58e83bc9"
# !! }}
users

# %%
# !! {"metadata":{
# !!   "id": "MY4cHUz8g3pr"
# !! }}
last_act = users[['user_id', 'action_date']][users['date_rank'] == 1]
last_act.rename(columns = {'action_date' : 'last'}, inplace = True)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 174
# !!   },
# !!   "id": "IbxpzYxZhjw8",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714272684058,
# !!     "user_tz": 360,
# !!     "elapsed": 137,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "46f845d2-44ec-4de4-fa21-8b1515365ba8"
# !! }}
last_act

# %%
# !! {"metadata":{
# !!   "id": "w7DUxu31h22m"
# !! }}
slast_act = users[['user_id', 'action_date']][users['date_rank'] == 2]
slast_act.rename(columns = {'action_date' : 'penultimate'}, inplace = True)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 143
# !!   },
# !!   "id": "7yMXUQQRiJLv",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714272854978,
# !!     "user_tz": 360,
# !!     "elapsed": 162,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "c10ce57f-3697-4dcb-d43f-afb25c957175"
# !! }}
slast_act

# %%
# !! {"metadata":{
# !!   "id": "bJyo_-Sti9tQ"
# !! }}
elapsed_days = pd.merge(last_act, slast_act, on = 'user_id', how = 'left').sort_values(by = 'user_id')
elapsed_days.reset_index(drop = True, inplace = True)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 244
# !!   },
# !!   "id": "ANUz5z9LovwM",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714273137821,
# !!     "user_tz": 360,
# !!     "elapsed": 165,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "03814605-a0be-4509-b7b5-1b60cb9eaa73"
# !! }}
elapsed_days

# %%
# !! {"metadata":{
# !!   "id": "B2yqdRRdpO93"
# !! }}
elapsed_days['elapsed_time'] = elapsed_days['last'] - elapsed_days['penultimate']

# %%
# !! {"metadata":{
# !!   "id": "0VYWJajQpy5Q",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714273338396,
# !!     "user_tz": 360,
# !!     "elapsed": 136,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "26a79a8d-5f40-4881-e62a-f938e8c88191",
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 264
# !!   }
# !! }}
elapsed_days

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 174
# !!   },
# !!   "id": "NX5wsYlHqKZB",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714273693330,
# !!     "user_tz": 360,
# !!     "elapsed": 434,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "59e3956e-c18f-4388-ded8-ff9caefe09ac"
# !! }}
elapsed_days[['user_id', 'elapsed_time']].sort_values(by = 'user_id')

# %%
# !! {"main_metadata":{
# !!   "colab": {
# !!     "provenance": [],
# !!     "authorship_tag": "ABX9TyMGZ7Pb+fweipL9FVKEwQX4"
# !!   },
# !!   "kernelspec": {
# !!     "name": "python3",
# !!     "display_name": "Python 3"
# !!   },
# !!   "language_info": {
# !!     "name": "python"
# !!   }
# !! }}

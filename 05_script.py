# %%
# !! {"metadata":{
# !!   "id": "5oy7WH_Qv7tE"
# !! }}
"""
# 05.Super users.
A company defines its super users as those who have made at least two transactions. From the following table, write a query to return, for each user, the date when they become a superuser,ordered by oldest super users first. Users who are not super users should also be present in the table.
"""

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 320
# !!   },
# !!   "id": "mhflAI6nv8EY",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714603388355,
# !!     "user_tz": 360,
# !!     "elapsed": 942,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "6a5928a4-7a9f-4275-e6b9-d26dad55d6fe"
# !! }}
import pandas as pd
import numpy as  np

data = {'user_id'          : [1,2,1,3,1,2,4,3],
        'product_id'       : [101,105,111,121,101,105,101,105],
        'transaction_date' : ['12-FEB-20',
                              '13-FEB-20',
                              '14-FEB-20',
                              '15-FEB-20',
                              '16-FEB-20',
                              '17-FEB-20',
                              '16-FEB-20',
                              '15-FEB-20']
        }

users = pd.DataFrame(data)
users

# %%
# !! {"metadata":{
# !!   "id": "CZjaK0ABwLlN",
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/"
# !!   },
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714603393851,
# !!     "user_tz": 360,
# !!     "elapsed": 217,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "1fe04ed9-cd5c-401e-fdcb-15312fdee14b"
# !! }}
users['transaction_date'] = pd.to_datetime(users['transaction_date'])

# %%
# !! {"metadata":{
# !!   "id": "JsZgsBPQwzkj"
# !! }}
def row_num(x):
      x_s = pd.Series(x)
      row_n = range(1, len(x_s) + 1)
      return row_n

# %%
# !! {"metadata":{
# !!   "id": "OBA8IYJUxPO5"
# !! }}
users['transaction_rank'] = users.groupby('user_id')['transaction_date'].transform(row_num)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 320
# !!   },
# !!   "id": "4c-htXASWER2",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714603710940,
# !!     "user_tz": 360,
# !!     "elapsed": 192,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "a68118b9-d874-4480-8460-74ecfcae8f2c"
# !! }}
users

# %%
# !! {"metadata":{
# !!   "id": "WKEACeyVxlB2"
# !! }}
superusers = users[['user_id', 'transaction_date']][users['transaction_rank'] == 2]

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 143
# !!   },
# !!   "id": "uLnlotQizGdQ",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714603416716,
# !!     "user_tz": 360,
# !!     "elapsed": 204,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "79106fe3-0a7f-4d8c-de66-affd84584dd3"
# !! }}
superusers

# %%
# !! {"metadata":{
# !!   "id": "N5btzLXQV3ID"
# !! }}
id_df = users['user_id'].unique()
id_df = pd.DataFrame(id_df)
id_df.rename(columns = {0 : 'user_id'}, inplace = True)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 174
# !!   },
# !!   "id": "PsWnXtjDWTza",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714603990902,
# !!     "user_tz": 360,
# !!     "elapsed": 185,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "439da6d2-ae31-46a8-cd1c-fe9692290ff1"
# !! }}
id_df

# %%
# !! {"metadata":{
# !!   "id": "tt2OFStTXihq"
# !! }}
superusers_date = pd.merge(id_df, superusers, on = 'user_id', how = 'left')

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 174
# !!   },
# !!   "id": "hdznew_uX_56",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714604304147,
# !!     "user_tz": 360,
# !!     "elapsed": 246,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "5daf9fc6-f5c0-4193-d8e2-0c00ce565b76"
# !! }}
superusers_date.sort_values(by = 'transaction_date')

# %%
# !! {"main_metadata":{
# !!   "colab": {
# !!     "provenance": [],
# !!     "authorship_tag": "ABX9TyNRS8SlLQ2xKg6sSoofi5uW"
# !!   },
# !!   "kernelspec": {
# !!     "name": "python3",
# !!     "display_name": "Python 3"
# !!   },
# !!   "language_info": {
# !!     "name": "python"
# !!   }
# !! }}

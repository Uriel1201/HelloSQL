# %%
# !! {"metadata":{
# !!   "id": "M86gpHdVopB3"
# !! }}
"""
# 2. Changes in Net Worth
From the following table of transactions between two users, write a query to return the change in net worth for each user, ordered by decreasing net change.
"""

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 174
# !!   },
# !!   "id": "hDdPezqW6u-y",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714173686015,
# !!     "user_tz": 360,
# !!     "elapsed": 2046,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "42d6f480-0905-48e5-e02b-b773abc3d41c"
# !! }}
# pip install SQLAlchemy
# pip install cx_Oracle

import pandas as pd
import numpy  as np
# import cx_Oracle
# import sqlalchemy
# from sqlalchemy.exc import SQLAlchemyError

'''
try:
  engine = sqlalchemy.create_engine("oracle+cx_oracle://usr:pswd@localhost/?service_name=orclpdb1", arraysize=1000)

  table = """select * from transactions_p2""";
  transactions = pd.read_sql(table, engine)
  transactions

except SQLAlchemyError as e:
  print(e)
'''

# %%
# !! {"metadata":{
# !!   "id": "jxd4esLVq0uZ",
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 323
# !!   },
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714173689838,
# !!     "user_tz": 360,
# !!     "elapsed": 176,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "7bf8b17d-915a-40ef-b65b-b3f25e422030"
# !! }}
data = {'Sender'            : [5, 1, 2, 2, 3, 3, 1],
        'Receiver'          : [2, 3, 1, 3, 1, 2, 4],
        'Amount'            : [10, 15, 20, 25, 20, 15, 5],
        'Transaction_Date'  : ['12-FEB-20',
                               '13-FEB-20',
                               '13-FEB-20',
                               '14-FEB-20',
                               '15-FEB-20',
                               '15-FEB-20',
                               '16-FEB-20']
        }

transactions = pd.DataFrame(data)
transactions['Transaction_Date'] = pd.to_datetime(transactions['Transaction_Date'])
transactions

# %%
# !! {"metadata":{
# !!   "id": "XMcS-p7j8Ops"
# !! }}
debited_df = transactions[['Sender', 'Amount']].groupby('Sender').sum()
debited_df.rename(columns = {'Amount' : 'Debited'}, inplace = True)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 206
# !!   },
# !!   "id": "Nny26ZR9V3YE",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714173699155,
# !!     "user_tz": 360,
# !!     "elapsed": 146,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "363e6638-da4c-4ff8-cc67-41d93914361e"
# !! }}
debited_df

# %%
# !! {"metadata":{
# !!   "id": "Y8RA0irOTEpk"
# !! }}
credited_df = transactions[['Receiver', 'Amount']].groupby('Receiver').sum()
credited_df.rename(columns = {'Amount' : 'Credited'}, inplace = True)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 206
# !!   },
# !!   "id": "v89Oo19CWMEh",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714173704370,
# !!     "user_tz": 360,
# !!     "elapsed": 151,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "633439a6-e88a-440c-feae-2d38de624969"
# !! }}
credited_df

# %%
# !! {"metadata":{
# !!   "id": "kqNAYnR1TZ2-"
# !! }}
net_changes = pd.concat([debited_df, credited_df], axis = 1, join = 'outer')
net_changes['User_id'] = net_changes.index
net_changes['Debited'].fillna(0, inplace = True)
net_changes['Credited'].fillna(0, inplace = True)
col_ = ['User_id','Debited','Credited']
net_changes = net_changes[col_]

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 206
# !!   },
# !!   "id": "QESleMC1We_t",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714173713345,
# !!     "user_tz": 360,
# !!     "elapsed": 16,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "24740246-862f-4c6e-d15a-cfdf4faf019f"
# !! }}
net_changes

# %%
# !! {"metadata":{
# !!   "id": "fbhmLWAvtP0y"
# !! }}
net_changes['net_change'] = net_changes['Credited'] - net_changes['Debited']

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 206
# !!   },
# !!   "id": "KVslgefmud7M",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714174004655,
# !!     "user_tz": 360,
# !!     "elapsed": 166,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "a218752e-a980-4d99-aec0-85d7d203205a"
# !! }}
net_changes[['User_id', 'net_change']].sort_values(by = 'net_change', ascending = False)

# %%
# !! {"main_metadata":{
# !!   "colab": {
# !!     "provenance": [],
# !!     "authorship_tag": "ABX9TyMcgELRUBA3x5TjP+znuhnB"
# !!   },
# !!   "kernelspec": {
# !!     "name": "python3",
# !!     "display_name": "Python 3"
# !!   },
# !!   "language_info": {
# !!     "name": "python"
# !!   }
# !! }}

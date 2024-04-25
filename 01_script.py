# %%
# !! {"metadata":{
# !!   "id": "pb2s4sGTfKUO"
# !! }}
"""
# 01. Cancelation Rates
From the following table of user IDs, actions, and dates, write a query to return the publication and cancellation rate for each user.
"""

# %%
# !! {"metadata":{
# !!   "id": "daiZQJANfK2_",
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 209
# !!   },
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714084295653,
# !!     "user_tz": 360,
# !!     "elapsed": 244,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "62ebfad0-e371-4675-c2ca-3c82112d57de"
# !! }}
# pip install pandas
# pip install numpy
# pip install SQLAlchemy
# pip install cx_Oracle

import pandas as pd
import numpy  as np
# import cx_Oracle
# import sqlalchemy
# from sqlalchemy.exc import SQLAlchemyError

'''
01. Cancellation Rates.

Writing a query to return the publication and cancellation
rate for each user


try:
  engine = sqlalchemy.create_engine("oracle+cx_oracle://usr:pswd@localhost/?service_name=orclpdb1", arraysize=1000)

  table = """select * from users_p1""";
  users = pd.read_sql(table, engine)
  users

except SQLAlchemyError as e:
  print(e)
'''

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 331
# !!   },
# !!   "id": "iQ7zcNQLf_iL",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714084305963,
# !!     "user_tz": 360,
# !!     "elapsed": 176,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "7b298d52-e7ef-49f1-84d9-3c8fd2b3bb31"
# !! }}
data = {'user_id' :[1,1,2,1,1,2,3,3,4],
        'action'  :['start','cancel','start',
                    'start','publish','publish',
                    'start','cancel','start'],
        'dates'   :['01-JAN-20',
                    '02-JAN-20',
                    '03-JAN-20',
                    '03-JAN-20',
                    '04-JAN-20',
                    '04-JAN-20',
                    '05-JAN-20',
                    '06-JAN-20',
                    '07-JAN-20']
        }

users = pd.DataFrame(data)
users

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 664
# !!   },
# !!   "id": "Q0n86Eo3W2R_",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714084315994,
# !!     "user_tz": 360,
# !!     "elapsed": 366,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "70f386ef-0966-4138-fbd0-6a9248996703"
# !! }}
users['starts']    = np.where(users['action']=='start',  1,0)
users['cancels']   = np.where(users['action']=='cancel', 1,0)
users['publishes'] = np.where(users['action']=='publish',1,0)
users

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 194
# !!   },
# !!   "id": "YMJZ32h9Yaem",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714084350479,
# !!     "user_tz": 360,
# !!     "elapsed": 249,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "842c6f7f-8af0-4c03-9ddf-8c52fb7d3df1"
# !! }}
actions = users[['user_id','starts','cancels','publishes']].groupby('user_id').sum()
actions.reset_index(inplace = True)
actions

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 194
# !!   },
# !!   "id": "WEdvTOh2YipV",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1714084949438,
# !!     "user_tz": 360,
# !!     "elapsed": 774,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "894b000f-4c7a-4e19-ffc0-ee80b60859da"
# !! }}
actions['cancel_rate']  = actions['cancels']   / actions['starts']
actions['publish_rate'] = actions['publishes'] / actions['starts']

actions[['user_id','cancel_rate','publish_rate']]

# %%
# !! {"main_metadata":{
# !!   "colab": {
# !!     "provenance": [],
# !!     "authorship_tag": "ABX9TyPpNGhKzG4N2hbTlc9nhIE/"
# !!   },
# !!   "kernelspec": {
# !!     "name": "python3",
# !!     "display_name": "Python 3"
# !!   },
# !!   "language_info": {
# !!     "name": "python"
# !!   }
# !! }}

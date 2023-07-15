# pip install pandas
# pip install numpy
# pip install SQLAlchemy
# pip install cx_Oracle

import pandas as pd 
import numpy  as np
import cx_Oracle
import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError

'''
1. Cancellation Rates.

Writing a query to return the publication and cancellation 
rate for each user
'''

try:
  engine = sqlalchemy.create_engine("oracle+cx_oracle://usr:pswd@localhost/?service_name=orclpdb1", arraysize=1000)

  table = """select * from users_p1""";
  users = pd.read_sql(table, engine)
  users
except SQLAlchemyError as e:
  print(e)

users['starts']    = np.where(users['action']=='start',  1,0])
users['cancels']   = np.where(users['action']=='cancel', 1,0])
users['publishes'] = np.where(users['action']=='publish',1,0])

actions = users[['user_id','starts','cancels','publishes']].groupby('user_id').sum()
actions.reset_index(inplace = True)


actions['cancel_rate']  = actions['cancels']   / actions['starts']
actions['publish_rate'] = actions['publishes'] / actions['starts']

actions[['user_id','cancel_rate','publish_rate']]

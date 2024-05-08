"""
# 8. Upgrade rate by product action (hard)
Given the following two tables, return the fraction of users, 
rounded to two decimal places, who accessed feature two (type: F2 in events table) 
and upgraded to premium within the first 30 days of signing up.
"""

# pip install pandas
# pip install numpy
# pip install SQLAlchemy
# pip install cx_Oracle

import pandas as pd
import numpy  as np
import cx_Oracle
import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError

try:
  engine = sqlalchemy.create_engine("oracle+cx_oracle://usr:pswd@localhost/?service_name=orclpdb1", arraysize=1000)

  table1 = """select * from users_p8;"""
  users = pd.read_sql(table1, engine)
  users
  table2 = """select * from events_p8;"""
  events = pd.read_sql(table2, engine)
  events
  
  users['join_date'] = pd.to_datetime(users['join_date'])
  events['access_date'] = pd.to_datetime(events['access_date'])

  def row_num(x):
      x_s = pd.Series(x)
      row_n = range(1, len(x_s) + 1)
      return row_n

  events['access_rank'] = events.groupby('user_id')['access_date'].transform(row_num)

  c1 = events['Type'] == 'F2'
  c2 = events['access_rank'] == 1
  first_F2 = events.loc[c1 & c2, ['user_id', 'access_date']]

  first_F2.set_index('user_id', inplace = True)
  users.set_index('user_id', inplace = True)

  c = events['Type'] == 'P'
  premium_users = events.loc[c, ['user_id', 'access_date']]
  premium_users.set_index('user_id', inplace = True)
  premium_users.rename(columns = {'access_date' : 'access_premium_date'}, inplace = True)

  F2_users = pd.concat([users, first_F2], axis = 1, join = 'inner')
  F2_toP = pd.merge(F2_users, premium_users, left_index = True, right_index = True, how = 'left')

  i = (np.where(F2_toP['access_premium_date'] - F2_toP['join_date'] <= pd.to_timedelta('30 days'), 1, 0).sum() / len(F2_toP.index)).round(2)
  d = {'upgrade_rate' : [i]
      }
  upgrade = pd.DataFrame(data = d, index = [0])
  upgrade

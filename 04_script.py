"""
# 04. Time difference between latest actions.

From the following table of user actions, 
write a query to return for each user the time elapsed 
between the last action and the second-to-last action, 
in ascending order by user ID.
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

  table = """select * from users_p4""";
  users = pd.read_sql(table, engine)
  users
  
  users['action_date'] = pd.to_datetime(users['action_date'])

  # Defining a function to count in descending order
  def row_num(x):
      x_s = pd.Series(x)
      row_n = range(len(x), 0, -1)
      return row_n

  users['date_rank'] = users.groupby('user_id')['action_date'].transform(row_num)

  last_act = users[['user_id', 'action_date']][users['date_rank'] == 1]
  last_act.rename(columns = {'action_date' : 'last'}, inplace = True)

  slast_act = users[['user_id', 'action_date']][users['date_rank'] == 2]
  slast_act.rename(columns = {'action_date' : 'penultimate'}, inplace = True)

  elapsed_days = pd.merge(last_act, slast_act, on = 'user_id', how = 'left').sort_values(by = 'user_id')
  elapsed_days.reset_index(drop = True, inplace = True)
  elapsed_days['elapsed_time'] = elapsed_days['last'] - elapsed_days['penultimate']

  elapsed_days[['user_id', 'elapsed_time']].sort_values(by = 'user_id')

"""
# 05.Super users.
A company defines its super users as those who have made at least 
two transactions. From the following table, write a query to return, 
for each user, the date when they become a superuser,ordered by oldest super users first.
Users who are not super users should also be present in the table.
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

  table = """select * from users_p5""";
  users = pd.read_sql(table, engine)
  users
  users['transaction_date'] = pd.to_datetime(users['transaction_date'])

  def row_num(x):
      x_s = pd.Series(x)
      row_n = range(1, len(x_s) + 1)
      return row_n

  users['transaction_rank'] = users.groupby('user_id')['transaction_date'].transform(row_num)

  superusers = users[['user_id', 'transaction_date']][users['transaction_rank'] == 2]

  id_df = users['user_id'].unique()
  id_df = pd.DataFrame(id_df)
  id_df.rename(columns = {0 : 'user_id'}, inplace = True)

  superusers_date = pd.merge(id_df, superusers, on = 'user_id', how = 'left')
  superusers_date.sort_values(by = 'transaction_date')

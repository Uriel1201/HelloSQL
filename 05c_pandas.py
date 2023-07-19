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
05. Super Users.

A company defines its super users as
those who have made at least two
transactions. 
Writing a query to return, for each user, the
date when they become a super user, ordered by oldest super users first.
Users who are not super users should
also be present in the table. 
'''

try:
  engine = sqlalchemy.create_engine("oracle+cx_oracle://usr:pswd@localhost/?service_name=orclpdb1", arraysize=1000)
  data = """select * from users_p5""";
  users = pd.read_sql(data, engine)
  users
  
except SQLAlchemyError as e:
  print(e)

users.info()
users['transaction_date'] = pd.to_datetime(users['transaction_date'])
users['ranks'] = users.groupby('user_id')['transaction_date'].rank(method = 'first')

distinct = pd.DataFrame(users['user_id'].unique())
distinct.rename(columns = {0:'user_id'}, inplace = True)

supers = users[users.ranks == 2.0][['user_id','transaction_date']]

pd.merge(distinct, supers, on = 'user_id', how = 'left').sort_values(by = 'transaction_date')

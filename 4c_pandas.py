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
04. Time Difference Between Latest Actions

writing a query to return for each user the
time elapsed between the last action
and the second-to-last action, in
ascending order by user ID. 
'''

try:
  engine = sqlalchemy.create_engine("oracle+cx_oracle://usr:pswd@localhost/?service_name=orclpdb1", arraysize=1000)
  data = """select * from users_p4""";
  users = pd.read_sql(data, engine)
  users
  
except SQLAlchemyError as e:
  print(e)

users['action_date'] = pd.to_datetime(users['action_date'])
users['ranks'] = users.groupby('user_id')['action_date'].rank(method = 'first', ascending = False) 
last_action = users[users.ranks == 1][['user_id','action_date']]
last_action.rename(columns = {'action_date':'last_action_date'}, inplace = True)
second_last_action = users[users.ranks == 2][['user_id','action_date']]
second_last_action.rename(columns = {'action_date':'second_last_action_date'}, inplace = True)
elapsed_days = pd.merge(last_action, second_last_action, on = 'user_id', how = 'left').sort_values(by = 'user_id')
elapsed_days.resest_index(inplace = True)
elapsed_days["elapsed_days'] = elapsed_days['last_action_date'] - elapsed_days['second_last_action_date']
elapsed_days[['user_id','elapsed_days']]

"""
# 9. Most friended
Given the following table, return a list of users and 
their corresponding friend count. 
Order the result by descending friend count, 
and in the case of a tie, by ascending user ID.
Assume that only unique friendships are displayed
"""

# pip install SQLAlchemy
# pip install cx_Oracle

import pandas as pd
import numpy  as np
import cx_Oracle
import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError

try:
  engine = sqlalchemy.create_engine("oracle+cx_oracle://usr:pswd@localhost/?service_name=orclpdb1", arraysize=1000)

  table = """select * from friends_p9;"""
  friends= pd.read_sql(table, engine)
  friends

  friend_counts = pd.DataFrame(pd.concat([friends['user_1'], friends['user_2']]))
  friend_counts = pd.DataFrame(friend_counts.groupby(0).size())
  friend_counts.rename(columns = {0 : 'number_friends'}, inplace = True)
  friend_counts.reset_index(inplace = True)
  friend_counts.rename(columns = {0 : 'user_id'}, inplace = True)

  friend_counts
  
except SQLAlchemyError as e:
  print(e)

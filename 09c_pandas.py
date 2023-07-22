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
09. Most Friended.

Returning a list of
users and their corresponding friend
count. Assuming that only
unique friendships are displayed.
'''

try:
  engine     = sqlalchemy.create_engine("oracle+cx_oracle://usr:pswd@localhost/?service_name=orclpdb1", arraysize=1000)
  data       = """select * from friends_p9""";

  friends    = pd.read_sql(data, engine)
  
except SQLAlchemyError as e:
  print(e)

u1           = friends['user_1'].copy()
u2           = friends['user_2'].copy()

users        = pd.DataFrame(pd.concat([u1, u2], ignore_index = True))
users.rename(columns = {0:'user_id'}, inplace = True)

user_friends = (users.groupby('user_id').agg({'user_id':np.size})).copy()
user_friends.rename(columns = {'user_id':'num_of_friends'}, inplace = True)
user_friends.reset_index(inplace = True)
user_friends.sort_values(['num_of_friends','user_id'], ascending = [False, True])

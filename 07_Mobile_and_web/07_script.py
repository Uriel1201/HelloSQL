"""
# 7. Mobile and web visitors
With the following two tables, return the fraction of users 
who only visited mobile, only visited web, and visited both.
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

  table = """select * from users_p1""";
  mobile = pd.read_sql(table, engine)
  mobile

  web

  mobile_users = pd.DataFrame(mobile['user_id'].drop_duplicates())
  web_users = pd.DataFrame(web['user_id'].drop_duplicates())
  mobile_users['mobile_user'] = mobile_users['user_id']
  web_users['web_user'] = web_users['user_id']
  mobile_users.set_index('user_id', inplace = True)
  web_users.set_index('user_id', inplace = True)

  matches = pd.concat([mobile_users, web_users], axis = 1, join = 'outer')
  matches['only_mobile'] = np.where(np.logical_and(~np.isnan(matches['mobile_user']), np.isnan(matches['web_user'])), True, False)
  matches['only_web'] = np.where(np.logical_and(~np.isnan(matches['web_user']), np.isnan(matches['mobile_user'])), True, False)
  matches['both'] = np.where(np.logical_and(~np.isnan(matches['mobile_user']), ~np.isnan(matches['web_user'])), True, False)

  matches = matches[['only_mobile', 'only_web', 'both']]

  pd.DataFrame(matches.mean())

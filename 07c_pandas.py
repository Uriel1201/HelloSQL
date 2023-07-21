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
07. Mobile and Web Visitors.

Returning the
fraction of users who only visited
mobile, only visited web, and visited
both. 
'''

try:
  engine = sqlalchemy.create_engine("oracle+cx_oracle://usr:pswd@localhost/?service_name=orclpdb1", arraysize=1000)
  data1 = """select * from mobile_p7""";
  data2 = """select * from web_p7""";

  mobile = pd.read_sql(data1, engine)
  web    = pd.read_sql(data2, engine)
  
except SQLAlchemyError as e:
  print(e)

index = 'user_id'
mobile_users              = pd.DataFrame(mobile[index].copy())
mobile_users['mobile_id'] = mobile[index]
web_users                 = pd.DataFrame(web[index].copy())
web_users['web_id']       = web[index]

tallies                = pd.merge(mobile_users, web_users, on = 'user_id', how = 'outer')
tallies                = tallies.drop_duplicates()
tallies['mobile_id']   = tallies['mobile_id'].replace(np.nan, 0).astype(int)
tallies['web_id']      = tallies['web_id'].replace(np.nan,    0).astype(int)
tallies['only_mobile'] = np.where(tallies['mobile_id']  > tallies['web_id'], 1, 0)
tallies['only_web']    = np.where(tallies['mobile_id']  < tallies['web_id'], 1, 0)
tallies['both']        = np.where(tallies['mobile_id'] == tallies['web_id'], 1, 0)
tallies                = tallies[['user_id','only_mobile','only_web','both']].copy()

averages = pd.DataFrame(tallies[['only_mobile','only_web','both']].mean().copy())
averages.rename(columns = {0:'average'}, inplace = True)

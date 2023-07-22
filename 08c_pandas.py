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
08. Upgrade Rate by Product Action

Returning the fraction of users, rounded to two
decimal places, who first accessed feature
two (type: F2 in events table) and
upgraded to premium within the first 30
days of signing up.
'''

try:
  engine = sqlalchemy.create_engine("oracle+cx_oracle://usr:pswd@localhost/?service_name=orclpdb1", arraysize=1000)
  data1  = """select * from users_p8""";
  data2  = """select * from events_p8""";

  users  = pd.read_sql(data1, engine)
  events = pd.read_sql(data2, engine)
  
except SQLAlchemyError as e:
  print(e)

users.info()
events.info()

users['join_date']    = pd.to_datetime(users['join_date'])
events['access_date'] = pd.to_datetime(events['access_date'])

events['rank']        = events.groupby('user_id')['access_date'].rank(method = 'first')
f1                    = np.where((events['rank'] == 1.0) & (events['Type'] == 'F2'))
F2_first              = pd.DataFrame(events.loc[f1])

Premium_access        = events[events.Type == 'P'][['user_id','access_date']].copy()
Premium_access.rename(columns = {'access_date':'Premium_access_date'}, inplace = True)

F2_first              = pd.merge(F2_first, Premium_access, on = 'user_id', how = 'left')
F2_first              = pd.merge(F2_first, users,          on = 'user_id', how = 'left')

i                     = (np.where(F2_first['Premium_access_date'] - F2_first['join_date'] <= pd.to_timedelta('30 days'), 1, 0).sum() / len(F2_first.index)).round(2)
d                     = {'upgrade_rate' : [i]
                        }
upgrade               = pd.DataFrame(data = d, index = [0])
upgrade 

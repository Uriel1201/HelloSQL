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
  users = pd.read_sql(table, engine)
  users
except SQLAlchemyError as e:
  print(e)

'''
still don't you have the table in any database?
data = {'user_id': [1,1,2,1,1,2,3,3,4],
        'action' : ['start','cancel','start','start',
                    'publish','publish','start','cancel','start'],
        'dates'  : ['01-JAN-20','02-JAN-20','03-JAN-20','03-JAN-20',
                    '04-JAN-20','04-JAN-20','05-JAN-20','06-JAN-20',
                    '07-JAN-20']
        }
users = pd.DataFrame(data)
users
'''

users['starts']    = np.where(users['action']=='start',  1,0])
users['cancels']   = np.where(users['action']=='cancel', 1,0])
users['publishes'] = np.where(users['action']=='publish',1,0])
users

num_actions = users.groupby('user_id').sum()
num_actions['cancel_rate']  = num_actions['cancels'] / num_actions['starts']
num_actions['publish_rate'] = num_actions['publishes'] / num_actions['starts']

num_actions[['publish_rate','cancel_rate']]

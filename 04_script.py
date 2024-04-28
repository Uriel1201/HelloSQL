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

  table = """select * from items_p3""";
  items = pd.read_sql(table, engine)

import pandas as pd
import numpy as  np

data = {'user_id' : [1,1,2,2,3,3,4,1],
        'actions'    : ['start','cancel','start',
                    'publish','start','cancel',
                    'start','publish'],
        'action_date'   : ['12-FEB-20',
                         '13-FEB-20',
                         '11-FEB-20',
                         '14-FEB-20',
                         '15-FEB-20',
                         '15-FEB-20',
                         '18-FEB-20',
                         '19-FEB-20']
        }

users = pd.DataFrame(data)
users

users['action_date'] = pd.to_datetime(users['action_date'])

users

def row_num(x):
    x_s = pd.Series(x)
    row_n = range(len(x), 0, -1)
    return row_n

users['date_rank'] = users.groupby('user_id')['action_date'].transform(row_num)

users

last_act = users[['user_id', 'action_date']][users['date_rank'] == 1]
last_act.rename(columns = {'action_date' : 'last'}, inplace = True)

last_act


slast_act = users[['user_id', 'action_date']][users['date_rank'] == 2]
slast_act.rename(columns = {'action_date' : 'penultimate'}, inplace = True)


slast_act

elapsed_days = pd.merge(last_act, slast_act, on = 'user_id', how = 'left').sort_values(by = 'user_id')
elapsed_days.reset_index(drop = True, inplace = True)


elapsed_days

elapsed_days['elapsed_time'] = elapsed_days['last'] - elapsed_days['penultimate']

# %%

elapsed_days


elapsed_days[['user_id', 'elapsed_time']].sort_values(by = 'user_id')

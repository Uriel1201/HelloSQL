"""
# 05.Super users.
A company defines its super users as those who have made at least 
two transactions. From the following table, write a query to return, 
for each user, the date when they become a superuser,ordered by oldest super users first.
Users who are not super users should also be present in the table.
"""

import pandas as pd
import numpy as  np

data = {'user_id'          : [1,2,1,3,1,2,4,3],
        'product_id'       : [101,105,111,121,101,105,101,105],
        'transaction_date' : ['12-FEB-20',
                              '13-FEB-20',
                              '14-FEB-20',
                              '15-FEB-20',
                              '16-FEB-20',
                              '17-FEB-20',
                              '16-FEB-20',
                              '15-FEB-20']
        }

users = pd.DataFrame(data)
users


users['transaction_date'] = pd.to_datetime(users['transaction_date'])

def row_num(x):
      x_s = pd.Series(x)
      row_n = range(1, len(x_s) + 1)
      return row_n

users['transaction_rank'] = users.groupby('user_id')['transaction_date'].transform(row_num)

users
superusers = users[['user_id', 'transaction_date']][users['transaction_rank'] == 2]
superuser
id_df = users['user_id'].unique()
id_df = pd.DataFrame(id_df)
id_df.rename(columns = {0 : 'user_id'}, inplace = True)

id_df

superusers_date = pd.merge(id_df, superusers, on = 'user_id', how = 'left')

superusers_date.sort_values(by = 'transaction_date')

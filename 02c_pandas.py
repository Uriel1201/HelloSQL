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
1. Changes in Net Worth

Writing a query to return the change in net worth for each user, 
ordered by decreasing net change.
'''

try:
  engine = sqlalchemy.create_engine("oracle+cx_oracle://usr:pswd@localhost/?service_name=orclpdb1", arraysize=1000)

  table = """select * from transactions_p2""";
  transactions = pd.read_sql(table, engine)
  transactions
except SQLAlchemyError as e:
  print(e)

debited  = transactions[['sender','amount']].groupby('sender').sum()
credited = transactions[['receicer','amount']].groupby('receiver').sum()

debited.reset_index(inplace  = True)
credited.reset_index(inplace = True)

debited.rename(columns  = {'sender'  :'user_id', 'amount':'debited'},  inplace = True)
credited.rename(columns = {'receiver':'user_id', 'amount':'credited'}, inplace = True)

changes = pd.merge(debited, credited, on = 'user_id', how = 'outer')
changes['debited']  = changes['debited'].replace(np.nan, 0)
changes['credited'] = changes['credited'].replace(np.nan,0)

changes['net_change'] = changes['credited'] - changes['debited'] 
changes[['user_id','net_change']].sort_values(by = 'net_change', ascending = False)

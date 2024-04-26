"""
# 2. Changes in Net Worth
From the following table of transactions between two users, 
write a query to return the change in net worth for each user, 
ordered by decreasing net change.
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

  table = """select * from transactions_p2""";
  transactions = pd.read_sql(table, engine)
  transactions
  transactions['Transaction_Date'] = pd.to_datetime(transactions['Transaction_Date'])

  debited_df = transactions[['Sender', 'Amount']].groupby('Sender').sum()
  debited_df.rename(columns = {'Amount' : 'Debited'}, inplace = True)

  credited_df = transactions[['Receiver', 'Amount']].groupby('Receiver').sum()
  credited_df.rename(columns = {'Amount' : 'Credited'}, inplace = True)

  net_changes = pd.concat([debited_df, credited_df], axis = 1, join = 'outer')
  net_changes['User_id'] = net_changes.index
  net_changes['Debited'].fillna(0, inplace = True)
  net_changes['Credited'].fillna(0, inplace = True)
  col_ = ['User_id','Debited','Credited']
  net_changes = net_changes[col_]
  net_changes['net_change'] = net_changes['Credited'] - net_changes['Debited']
  net_changes[['User_id', 'net_change']].sort_values(by = 'net_change', ascending = False)

except SQLAlchemyError as e:
  print(e)

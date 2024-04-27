"""
# 03. Most Frequent Items
From the following table containing a list of dates and items ordered, write a query to return the most frequent item ordered on each date. Return multiple items in the case of a tie.
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
  items

  items['dates'] = pd.to_datetime(items['dates'])

  item_counts = items.groupby(['dates', 'item']).size().reset_index(name = 'counts')
  item_counts['item_rank'] = item_counts.groupby('dates')['counts'].rank(method = 'dense', ascending = False)
  item_counts[['dates', 'item']][item_counts['item_rank'] == 1.0]

except SQLAlchemyError as e:
  print(e)

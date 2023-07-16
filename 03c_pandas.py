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
03. Most Frequent Item

Writing a query to return the most frequent item
ordered on each date.
'''

try:
  engine = sqlalchemy.create_engine("oracle+cx_oracle://usr:pswd@localhost/?service_name=orclpdb1", arraysize=1000)
  data = """select * from items_p3""";
  items = pd.read_sql(data, engine)
  items
  
except SQLAlchemyError as e:
  print(e)

item_counts = items.groupby(['dates','item']).agg({'item':np.size})
item_counts.rename(columns = {'item':'count'}, inplace = True)
item_counts.reset_index(inplace = True)
item_counts['ranks'] = item_counts.group.by('dates')['count'].rank(method = 'min', ascending = False)

item_counts[item_counts.ranks == 1.0][['dates','item']]

#<cc-imports>
import subprocess

sub_p_res = subprocess.run(['wget', 'https://raw.githubusercontent.com/Uriel1201/HelloSQL/main/functions_df.p'], stdout=subprocess.PIPE).stdout.decode('utf-8') #<cc-cm>
print(sub_p_res) #<cc-cm>

"""
# 13. Rank without RANK (hard)
Write a query to rank scores in the following table without using a window function. 
If there is a tie between two scores, both should have the same rank. 
After a tie, the following rank should be the next consecutive integer value.
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

  table = """select * from scores_p13;"""
  scores = pd.read_sql(table, engine)
  scores

  score_array = np.array(scores['score'])

  """
  Using my own rank_serie method to asign ranks on an array.
  """

  rank_df = pd.DataFrame(fd.rank_serie(score_array), columns = ['score', 'rank'])
  rank_df.sort_values(by = 'rank')

except SQLAlchemyError as e:
  print(e)

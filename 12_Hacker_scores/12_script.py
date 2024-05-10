# !pip install wget
import subprocess

"""
# 12. Hacker scores
Given the following two tables, write a query to return the hacker ID, name, 
and total score (the sum of maximum scores for each challenge completed) ordered by descending score, 
and by ascending hacker ID in the case of score tie. 
Do not display entries for hackers with a score of zero.
"""

sub_p_res = subprocess.run(['wget', 'https://raw.githubusercontent.com/Uriel1201/HelloSQL/main/function_df.py'], stdout=subprocess.PIPE).stdout.decode('utf-8') #<cc-cm>
print(sub_p_res) #<cc-cm>

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

  table1 = """select * from hackers_p12;"""
  hackers = pd.read_sql(table1, engine)
  hackers 

  table2 = """select * from submissions_p12;"""
  submissions = pd.read_sql(table2, engine)
  submissions

  submissions = submissions.sort_values(by = ['hacker_id', 'challenge_id', 'score'])
  submissions['score_rank'] = submissions.groupby(['hacker_id', 'challenge_id'])['score'].transform(f_df.desc_row_num)

  c = submissions['score_rank'] == 1
  max_scores = submissions.loc[c, ['hacker_id', 'score']]
  max_scores.set_index('hacker_id', inplace = True, drop = True)

  total_score = max_scores.groupby(level = 0).sum()
  total_score = total_score[total_score['score'] > 0]

  hackers.set_index('hacker_id', inplace = True, drop = True)

  hacker_scores = pd.concat([hackers, total_score], axis = 1, join = 'inner')
  hacker_scores = hacker_scores.sort_values(by = 'score', ascending = False)

except SQLAlchemyError as e:
  print(e)

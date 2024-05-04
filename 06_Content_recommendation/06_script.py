"""
#06. Content recommendation (hard)
Using the following two tables, write a query to return 
page recommendations to a social media user based on 
the pages that their friends have liked, but that 
they have not yet marked as liked. 
Order the result by ascending user ID.
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

  table1 = """select * from friends_p6;"""
  friends = pd.read_sql(table1, engine)
  table2 = """select * from likes_p6;"""
  likes = pd.read_sql(table2, engine)

  friends_likes = pd.merge(friends, likes, left_on = 'friend', right_on = 'user_id')
  friends_likes.drop('user_id_y', axis = 1, inplace = True)
  friends_likes.rename(columns = {'user_id_x' : 'user_id', 'page_likes' : 'friend_page_likes'}, inplace = True)
  friends_likes.set_index(['user_id', 'friend_page_likes'], inplace = True, drop = False)
  friends_likes.rename_axis(index = {'friend_page_likes' : 'page_likes'}, inplace = True)

  user_likes = likes.set_index(['user_id', 'page_likes'], drop = False)
  user_likes.drop('user_id', axis = 1, inplace = True)

  is_liked = pd.concat([friends_likes, user_likes], axis = 1, join = 'outer')

  recomendations = is_liked[['user_id']][is_liked['page_likes'].isnull()]
  recomendations.drop('user_id', axis = 1,inplace = True)
  recomendations.reset_index(inplace = True)
  recomendations.rename(columns = {'page_likes' : 'recommended_page'}, inplace = True)
  recomendations.drop_duplicates(inplace = True)

  recomendations.sort_values(by = 'user_id')

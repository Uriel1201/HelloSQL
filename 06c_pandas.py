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
06. Content Recommendations

Writing a query to return page recommendations
to a social media user based on the
pages that their friends have liked, but
that they have not yet marked as liked.
'''

try:
  engine = sqlalchemy.create_engine("oracle+cx_oracle://usr:pswd@localhost/?service_name=orclpdb1", arraysize=1000)
  data1 = """select * from friends_p6""";
  data2 = """select * from likes_p6""";

  friends = pd.read_sql(data1, engine)
  likes   = pd.read_sql(data2, engine)
  
except SQLAlchemyError as e:
  print(e)

likes['page_friend_likes'] = likes['page_likes']

i = ['user_id','page_friend_likes']

friend_likes = likes[i].copy()
friend_likes.rename(columns = {'user_id':'friend'}, inplace = True)

tallies = pd.merge(friends, friend_likes, on = 'friend', how = 'inner')
tallies.set_index(i)
likes.set_index(i)
tallies = pd.merge(tallies, likes, how = 'left')

recommendations = tallies[tallies.page_likes.isnull()][i].copy()
recommendations.rename(columns = {'page_friend_likes':'recommended_page'}, inplace = True)
recommendations.drop_duplicates().sort_values(by = 'user_id')

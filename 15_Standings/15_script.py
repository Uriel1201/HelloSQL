"""
# 15. Team standings
Write a query to return the scores of
each team in the teams table after all
matches displayed in the matches table.
Points are awarded as follows: zero
points for a loss, one point for a tie, and
three points for a win. The result should
include team name and points, and be
ordered by decreasing points.
"""

import pandas as pd
import numpy  as np
import cx_Oracle
import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError

try:
    engine = sqlalchemy.create_engine("oracle+cx_oracle://usr:pswd@localhost/?service_name=orclpdb1", arraysize=1000)

    table1 = """select * from teams_p15;"""
    table2 = """select * from matches_p15"""
    teams = pd.read_sql(table1, engine)
    matches = pd.read_sql(table2, engine)
    teams.set_index('team_id', inplace = True)

    host_matches = matches[['host_team', 'host_goals', 'guest_goals']].copy()
    host_matches.rename(columns = {'host_team' : 'team_id'}, inplace = True)
    host_matches['host_scores'] = np.where(host_matches['host_goals'] > host_matches['guest_goals'], 3 ,np.where(host_matches['host_goals'] == host_matches['guest_goals'], 1, 0))

    host_scores = pd.DataFrame(host_matches.groupby('team_id')['host_scores'].sum())

    guest_matches = matches[['guest_team', 'host_goals', 'guest_goals']].copy()
    guest_matches.rename(columns = {'guest_team' : 'team_id'}, inplace = True)
    guest_matches['guest_scores'] = np.where(guest_matches['guest_goals'] > guest_matches['host_goals'], 3 ,np.where(guest_matches['guest_goals'] == guest_matches['host_goals'], 1, 0))

    guest_scores = pd.DataFrame(guest_matches.groupby('team_id')['guest_scores'].sum())

    scores = pd.concat([host_scores, guest_scores], axis = 1, join = 'inner')
    scores = pd.DataFrame(scores['host_scores'] + scores['guest_scores'])
    scores.rename(columns = {0 : 'score'}, inplace = True)

    results = pd.concat([teams, scores], axis = 1, join = 'inner')
    results.sort_values(by = 'score', ascending = False)

except SQLAlchemyError as e:
  print(e)

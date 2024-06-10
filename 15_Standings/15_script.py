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

data1 = {'team_id' : [1,2,3,4,5,6],
         'team_name' : ['New York','Atlanta','Chicago','Toronto','Los Angeles','Seattle']
        }

data2 = {'match_id'    : [1,2,3,4,5,6],
         'host_team'   : [1,2,3,4,5,6],
         'guest_team'  : [2,3,4,5,6,1],
         'host_goals'  : [3,2,4,1,2,1],
         'guest_goals' : [0,4,3,1,1,2]
        }

teams   = pd.DataFrame(data1)
matches = pd.DataFrame(data2)

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

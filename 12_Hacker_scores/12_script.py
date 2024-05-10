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

import pandas as pd
import numpy  as np
import function_df as f_df

data1 = {'hacker_id' : [1,2,3,4],
         'name'      : ['John','Jane','Joe','Jim']
        }

data2 = {'sub_id'       : [101,102,103,104,105,106,107,108,109],
         'hacker_id'    : [1,1,2,2,2,3,3,3,4],
         'challenge_id' : [1,1,1,1,2,1,2,2,1],
         'score'        : [10,12,11,9,13,9,12,15,0]
        }

hackers     = pd.DataFrame(data1)
submissions = pd.DataFrame(data2)

submissions = submissions.sort_values(by = ['hacker_id', 'challenge_id', 'score'])
submissions['score_rank'] = submissions.groupby(['hacker_id', 'challenge_id'])['score'].transform(f_df.desc_row_num)

c = submissions['score_rank'] == 1
max_scores = submissions.loc[c, ['hacker_id', 'score']]
max_scores.set_index('hacker_id', inplace = True, drop = True)

total_score = max_scores.groupby(level=0).sum()
total_score = total_score[total_score['score'] > 0]

hackers.set_index('hacker_id', inplace = True, drop = True)

hacker_scores = pd.concat([hackers, total_score], axis = 1, join = 'inner')
hacker_scores.sort_values(by = 'score', ascending = False)

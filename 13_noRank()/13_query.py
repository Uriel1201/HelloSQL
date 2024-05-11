"""
Write a query to rank scores in the following table without using a window function. 
If there is a tie between two scores, both should have the same rank. 
After a tie, the following rank should be the next consecutive integer value.
"""

import pandas as pd
import numpy  as np

data = {'id'    : [1,2,3,4,5,6],
        'score' : [3.5,3.65,4.0,3.85,4.0,3.65]
       }

scores = pd.DataFrame(data)

scores

def rank_serie(serie):
    copy = np.array(serie.drop_duplicates())
    count_list = [np.sum(copy >= s) for s in serie]
    array_list = np.array(list(zip(serie, count_list)))
    return array_list

score_id = scores['score']
rank_score = pd.DataFrame(rank_serie(score_id), columns=['score', 'rank'])

rank_score

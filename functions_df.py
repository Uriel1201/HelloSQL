import pandas as pd
import numpy as np

#----------------------------------------------
def row_num(x):
    x_s = pd.Series(x)
    row_n = range(1, len(x_s) + 1)
    return row_n

#----------------------------------------------
def desc_row_num(x):
    x_s = pd.Series(x)
    row_n = range(len(x_s), 0, -1)
    return row_n

#----------------------------------------------
def rank_serie(seri):
    serie = np.array(seri)
    copy = np.unique(serie)
    count_list = [np.sum(copy >= s) for s in serie]
    array_list = np.array(list(zip(serie, count_list)))
    return array_list

#----------------------------------------------
def main():
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
    submissions['score_number'] = submissions.groupby(['hacker_id', 'challenge_id'])['score'].transform(row_num)
    submissions['score_rank'] = submissions.groupby(['hacker_id', 'challenge_id'])['score'].transform(desc_row_num)
    print(submissions)
    random_array = np.random.randint(1, 16, 30)
    r = rank_serie(random_array)
    r_R = pd.DataFrame(r, columns = ['score', 'rank'])
    r_R.sort_values(by = 'score')
#----------------------------------------------
if __name__ == '__main__':
    main()

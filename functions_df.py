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
def rank_array(Se):
    Se.drop_duplicates(inplace = True)
    s_array = np.array(Se)
    copy = np.unique(s_array)
    count_list = [np.sum(copy >= s) for s in s_array]
    array_list = np.array(list(zip(s_array, count_list)))
    return array_list

#----------------------------------------------
def basic_cummulative(table, index_col, col):
    copy = table.set_index(index_col)
    column_values = []
    n = copy.index.unique()
    for idx in n:
        values_serie = copy.loc[idx, col]
        if isinstance(values_serie, pd.Series):
            values_list = values_serie.tolist()
        else:
            values_list = [values_serie]
        column_values.append(values_list)
    max_length = max(len(v_l) for v_l in column_values)
    numpy_array = np.zeros((len(n), max_length))
    for i, values in enumerate(column_values):
        numpy_array[i, :len(values)] = values
    cumsum_array = np.cumsum(numpy_array, axis = 1)
    cumsum_df = pd.DataFrame(cumsum_array, index = n)
    return cumsum_df
    
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
    print("Dataframe Submissions")
    print("****************************")
    print(submissions)
    print()
    submissions = submissions.sort_values(by = ['hacker_id', 'challenge_id', 'score'])
    submissions['ascending_score'] = submissions.groupby(['hacker_id', 'challenge_id'])['score'].transform(row_num)
    submissions['descending_score'] = submissions.groupby(['hacker_id', 'challenge_id'])['score'].transform(desc_row_num)
    print("Adding ascending and descending counters to the scores grouped by hacker_id and challenge_id")
    print("****************************")
    print(submissions)
    print()
    scores = submissions['score']
    score_ranks = pd.DataFrame(rank_array(scores), columns = ['score', 'rank'])
    print("Adding a rank for every score")
    print("****************************")
    print(score_ranks)
    print()
    numpy_submissions = basic_cummulative(submissions, 'hacker_id', 'score')
    table2 = pd.DataFrame(numpy_submissions)
    print("Cummulative_scores Dataframe by hacker_id")
    print("****************************")
    print(table2)
    print()
#----------------------------------------------
if __name__ == '__main__':
    main()

# %%
# !! {"metadata":{
# !!   "id": "He2MrphpBhEh",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715288315441,
# !!     "user_tz": 360,
# !!     "elapsed": 718,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
import pandas as pd
import numpy as np

# %%
# !! {"metadata":{
# !!   "id": "_Ixvd4RyB0Fe",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715288317717,
# !!     "user_tz": 360,
# !!     "elapsed": 11,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
def row_num(x):
    x_s = pd.Series(x)
    row_n = range(1, len(x_s) + 1)
    return row_n

# %%
# !! {"metadata":{
# !!   "id": "7Ve91-5uCVm3",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715288320097,
# !!     "user_tz": 360,
# !!     "elapsed": 290,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
def desc_row_num(x):
    x_s = pd.Series(x)
    row_n = range(len(x_s), 0, -1)
    return row_n

# %%
# !! {"metadata":{
# !!   "id": "kBBROtAoKKUM",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715288717074,
# !!     "user_tz": 360,
# !!     "elapsed": 290,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
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

# %%
# !! {"metadata":{
# !!   "id": "YQC3-Mfv3sX3",
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/"
# !!   },
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715288719386,
# !!     "user_tz": 360,
# !!     "elapsed": 289,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "3ae562db-8f73-40a0-a5d7-d4e150b563f5"
# !! }}
if __name__ == '__main__':
    main()

# %%
# !! {"main_metadata":{
# !!   "colab": {
# !!     "provenance": [],
# !!     "authorship_tag": "ABX9TyMrtIqCLdPRPWyZNn0iw6Io"
# !!   },
# !!   "kernelspec": {
# !!     "name": "python3",
# !!     "display_name": "Python 3"
# !!   },
# !!   "language_info": {
# !!     "name": "python"
# !!   }
# !! }}

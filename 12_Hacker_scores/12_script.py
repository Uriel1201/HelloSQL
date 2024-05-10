# !pip install wget
import subprocess


"""
# 12. Hacker scores
Given the following two tables, write a query to return the hacker ID, name, and total score (the sum of maximum scores for each challenge completed) ordered by descending score, and by ascending hacker ID in the case of score tie. Do not display entries for hackers with a score of zero.
"""

sub_p_res = subprocess.run(['wget', 'https://raw.githubusercontent.com/Uriel1201/HelloSQL/main/function_df.p'], stdout=subprocess.PIPE).stdout.decode('utf-8') #<cc-cm>
print(sub_p_res) #<cc-cm>


# %%
# !! {"metadata":{
# !!   "id": "a5W6KbH13HFA",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715363559605,
# !!     "user_tz": 360,
# !!     "elapsed": 1193,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
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

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 174
# !!   },
# !!   "id": "vRX-gHSN4VtD",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715363562924,
# !!     "user_tz": 360,
# !!     "elapsed": 219,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "5635075e-c3d7-4079-ce56-68463b9a4eff"
# !! }}
hackers

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 351
# !!   },
# !!   "id": "47TUq80W4Zhp",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715363566038,
# !!     "user_tz": 360,
# !!     "elapsed": 228,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "4c6e08a3-44c0-4bee-d01e-380d8a017496"
# !! }}
submissions

# %%
# !! {"metadata":{
# !!   "id": "XaZI22nB4_dq",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715363569884,
# !!     "user_tz": 360,
# !!     "elapsed": 164,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
submissions = submissions.sort_values(by = ['hacker_id', 'challenge_id', 'score'])
submissions['score_rank'] = submissions.groupby(['hacker_id', 'challenge_id'])['score'].transform(f_df.desc_row_num)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 351
# !!   },
# !!   "id": "NxNF2CIP7DC8",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715363573044,
# !!     "user_tz": 360,
# !!     "elapsed": 172,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "ebfa7b44-0c31-49b1-acf4-943cb54e7f98"
# !! }}
submissions

# %%
# !! {"metadata":{
# !!   "id": "vKnxICSEZYvz",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715363577062,
# !!     "user_tz": 360,
# !!     "elapsed": 162,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
c = submissions['score_rank'] == 1
max_scores = submissions.loc[c, ['hacker_id', 'score']]
max_scores.set_index('hacker_id', inplace = True, drop = True)

# %%
# !! {"metadata":{
# !!   "id": "qcMz0YtXbLnw",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715363580497,
# !!     "user_tz": 360,
# !!     "elapsed": 165,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
total_score = max_scores.groupby(level=0).sum()
total_score = total_score[total_score['score'] > 0]

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 174
# !!   },
# !!   "id": "JZGwwZoe8mGr",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715363582716,
# !!     "user_tz": 360,
# !!     "elapsed": 173,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "cec55173-e74b-4b99-ba5d-c3a8b776e7e5"
# !! }}
total_score

# %%
# !! {"metadata":{
# !!   "id": "BaMA4CI68upa",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715363587159,
# !!     "user_tz": 360,
# !!     "elapsed": 195,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
hackers.set_index('hacker_id', inplace = True, drop = True)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 206
# !!   },
# !!   "id": "650LCokn-eyf",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715363593005,
# !!     "user_tz": 360,
# !!     "elapsed": 186,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "1cc17df8-042f-42f3-c50b-150925ba5abb"
# !! }}
hackers

# %%
# !! {"metadata":{
# !!   "id": "LAEuUrB1_BJY",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715363596755,
# !!     "user_tz": 360,
# !!     "elapsed": 160,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
hacker_scores = pd.concat([hackers, total_score], axis = 1, join = 'inner')

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 174
# !!   },
# !!   "id": "71qlz57u_Un8",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715363598754,
# !!     "user_tz": 360,
# !!     "elapsed": 144,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "26cf001a-7924-44cb-d7da-e2e3695a3a3b"
# !! }}
hacker_scores.sort_values(by = 'score', ascending = False)

# %%
# !! {"main_metadata":{
# !!   "colab": {
# !!     "provenance": [],
# !!     "authorship_tag": "ABX9TyNgvURaKmGgfWU+bIOrbKfS"
# !!   },
# !!   "kernelspec": {
# !!     "name": "python3",
# !!     "display_name": "Python 3"
# !!   },
# !!   "language_info": {
# !!     "name": "python"
# !!   }
# !! }}

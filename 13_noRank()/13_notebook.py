# %%
# !! {"metadata":{
# !!   "id":"cc-imports"
# !! }}

#<cc-imports>

import subprocess

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/"
# !!   },
# !!   "id": "FGJhR_QoO85a",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715457579006,
# !!     "user_tz": 360,
# !!     "elapsed": 22,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "722ce571-2d77-459c-8036-e379812b2696"
# !! }}
sub_p_res = subprocess.run(['wget', 'https://raw.githubusercontent.com/Uriel1201/HelloSQL/main/functions_df.p'], stdout=subprocess.PIPE).stdout.decode('utf-8') #<cc-cm>
print(sub_p_res) #<cc-cm>


# %%
# !! {"metadata":{
# !!   "id": "QrPYPRs5O_16"
# !! }}
"""
# 13. Rank without RANK (hard)
Write a query to rank scores in the following table without using a window function. If there is a tie between two scores, both should have the same rank. After a tie, the following rank should be the next consecutive integer value.
"""

# %%
# !! {"metadata":{
# !!   "id": "cRF_eQNNPA6o",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715457645487,
# !!     "user_tz": 360,
# !!     "elapsed": 758,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
import pandas as pd
import numpy  as np
import functions_df as fd

data = {'id'    : [1,2,3,4,5,6],
        'score' : [3.5,3.65,4.0,3.85,4.0,3.65]
       }

scores = pd.DataFrame(data)

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 237
# !!   },
# !!   "id": "B2yElLxlPmR6",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715457652646,
# !!     "user_tz": 360,
# !!     "elapsed": 198,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "92b32132-091c-4e2d-ce47-1f78a0b634de"
# !! }}
scores

# %%
# !! {"metadata":{
# !!   "id": "f3ve_TXdPqUF",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715457706593,
# !!     "user_tz": 360,
# !!     "elapsed": 149,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
score_array = np.array(scores['score'])

# %%
# !! {"metadata":{
# !!   "id": "e7ex9sbRR0yp"
# !! }}
"""
Using my own rank_serie method to asign ranks on an array.
"""

# %%
# !! {"metadata":{
# !!   "id": "XdF8CmJgP1w1",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715457841521,
# !!     "user_tz": 360,
# !!     "elapsed": 171,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   }
# !! }}
rank_df = pd.DataFrame(fd.rank_serie(score_array), columns = ['score', 'rank'])

# %%
# !! {"metadata":{
# !!   "colab": {
# !!     "base_uri": "https://localhost:8080/",
# !!     "height": 237
# !!   },
# !!   "id": "-JHEFCqHQWUg",
# !!   "executionInfo": {
# !!     "status": "ok",
# !!     "timestamp": 1715457885256,
# !!     "user_tz": 360,
# !!     "elapsed": 223,
# !!     "user": {
# !!       "displayName": "Uriel Garc\u00eda",
# !!       "userId": "03386744220426758265"
# !!     }
# !!   },
# !!   "outputId": "4ac69766-e4f7-4f5a-9a3f-543203c2ec69"
# !! }}
rank_df.sort_values(by = 'rank')

# %%
# !! {"main_metadata":{
# !!   "colab": {
# !!     "provenance": [],
# !!     "authorship_tag": "ABX9TyPD47zsfkm+Gkbg5H9tP1/8"
# !!   },
# !!   "kernelspec": {
# !!     "name": "python3",
# !!     "display_name": "Python 3"
# !!   },
# !!   "language_info": {
# !!     "name": "python"
# !!   }
# !! }}

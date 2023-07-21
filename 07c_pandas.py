index = 'user_id'
mobile_users = pd.DataFrame(mobile[index].copy())
mobile_users['mobile_id'] = mobile[index]
web_users = pd.DataFrame(web[index].copy())
web_users['web_id'] = web[index]

tallies                = pd.merge(mobile_users, web_users, on = 'user_id', how = 'outer')
tallies                = tallies.drop_duplicates()
tallies['mobile_id']   = tallies['mobile_id'].replace(np.nan, 0).astype(int)
tallies['web_id']      = tallies['web_id'].replace(np.nan,    0).astype(int)
tallies['only_mobile'] = np.where(tallies['mobile_id']  > tallies['web_id'], 1, 0)
tallies['only_web']    = np.where(tallies['mobile_id']  < tallies['web_id'], 1, 0)
tallies['both']        = np.where(tallies['mobile_id'] == tallies['web_id'], 1, 0)
tallies                = tallies[['user_id','only_mobile','only_web','both']].copy()

averages = pd.DataFrame(tallies[['only_mobile','only_web','both']].mean().copy())
averages.rename(columns = {0:'average'}, inplace = True)

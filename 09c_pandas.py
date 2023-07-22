u1           = friends['user_1'].copy()
u2           = friends['user_2'].copy()

users        = pd.DataFrame(pd.concat([u1, u2], ignore_index = True))
users.rename(columns = {0:'user_id'}, inplace = True)

user_friends = (users.groupby('user_id').agg({'user_id':np.size})).copy()
user_friends.rename(columns = {'user_id':'num_of_friends'}, inplace = True)
user_friends.reset_index(inplace = True)
user_friends.sort_values(['num_of_friends','user_id'], ascending = [False, True])

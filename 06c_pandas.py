likes['page_friend_likes'] = likes['page_likes']

i = ['user_id','page_friend_likes']

friend_likes = likes[i].copy()
friend_likes.rename(columns = {'user_id':'friend'}, inplace = True)

tallies = pd.merge(friends, friend_likes, on = 'friend', how = 'inner')
tallies.set_index(i)
likes.set_index(i)
tallies = pd.merge(tallies, likes, how = 'left')

recommendations = tallies[tallies.page_likes.isnull()][i].copy()
recommendations.rename(columns = {'page_friend_likes':'recommended_page'}, inplace = True)
recommendations.drop_duplicates().sort_values(by = 'user_id')

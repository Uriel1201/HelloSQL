
"""
#06. Content recommendation (hard)
Using the following two tables, write a query to return 
page recommendations to a social media user based on 
the pages that their friends have liked, but that 
they have not yet marked as liked. 
Order the result by ascending user ID.
"""



friends


likes


friends_likes = pd.merge(friends, likes, left_on = 'friend', right_on = 'user_id')


friends_likes


friends_likes.drop('user_id_y', axis = 1, inplace = True)
friends_likes.rename(columns = {'user_id_x' : 'user_id', 'page_likes' : 'friend_page_likes'}, inplace = True)


friends_likes


friends_likes.set_index(['user_id', 'friend_page_likes'], inplace = True, drop = False)
user_likes = likes.set_index(['user_id', 'page_likes'], drop = False)


friends_likes.rename_axis(index = {'friend_page_likes' : 'page_likes'}, inplace = True)

friends_likes


user_likes


user_likes.drop('user_id', axis = 1, inplace = True)


user_likes


is_liked = pd.concat([friends_likes, user_likes], axis = 1, join = 'outer')


is_liked


recomendations = is_liked[['user_id']][is_liked['page_likes'].isnull()]


recomendations.drop('user_id', axis = 1,inplace = True)
recomendations.reset_index(inplace = True)


recomendations.rename(columns = {'page_likes' : 'recommended_page'}, inplace = True)
recomendations.drop_duplicates(inplace = True)


recomendations.sort_values(by = 'user_id')

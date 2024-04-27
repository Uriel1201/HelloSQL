"""
# 03. Most Frequent Items
From the following table containing a list of dates and items ordered, write a query to return the most frequent item ordered on each date. Return multiple items in the case of a tie.
"""

import pandas as pd
import numpy as  np

data = {'dates' : ['01-JAN-20',
                   '01-JAN-20',
                   '01-JAN-20',
                   '01-JAN-20',
                   '02-JAN-20',
                   '02-JAN-20',
                   '02-JAN-20',
                   '02-JAN-20'],
        'item' : ['apple',
                  'apple',
                  'pear',
                  'pear',
                  'pear',
                  'pear',
                  'pear',
                  'orange']

       }
items = pd.DataFrame(data)
items


items['dates'] = pd.to_datetime(items['dates'])

item_counts = items.groupby(['dates', 'item']).size().reset_index(name = 'counts')
item_counts['item_rank'] = item_counts.groupby('dates')['counts'].rank(method = 'dense', ascending = False)
item_counts[['dates', 'item']][item_counts['item_rank'] == 1.0]

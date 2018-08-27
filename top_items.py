"""
Simple, rating based recommender system
Simple recommender system based on ratings.
This can be used when the user has not bought anything yet.

Params for the formula:
v - number of votes
m - min number of votes required
r - average rating
c - mean of average rating
"""

import pandas as pd

def get_top_items(dataset):
    
    data = pd.DataFrame(dataset)
    # Recommender system params
    C = data['vote_average'].mean()
    m = data['vote_count'].quantile(0.10) # min nr of votes needed. The higher, the less movies

    # Filter out unqualified data
    f_data = data.copy().loc[data['vote_count'] > m]

    def weighted_rating(x, m=m, c=C):
        v = x['vote_count']
        r = x['vote_average']
        # IMDB formula
        return (v/(v+m))*r + (m/(v+m))*c
    
    f_data['score'] = f_data.apply(weighted_rating, axis=1)
    f_data = f_data.sort_values('score', ascending=False)

    f_data = f_data.drop(columns=['score'])

    return f_data.to_json(orient='records')

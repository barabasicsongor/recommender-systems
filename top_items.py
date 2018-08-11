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

def get_dataset():
    X = [{'name': 'X-Man', 'vote_average': 7.7, 'vote_count': 5400},
         {'name': 'Catwoman', 'vote_average': 8.1, 'vote_count': 10},
         {'name': 'Wolf', 'vote_average': 6.5, 'vote_count': 200},
         {'name': 'Titanic', 'vote_average': 6.5, 'vote_count': 3200},
         {'name': 'Honolulu', 'vote_average': 10, 'vote_count': 4}]

    return pd.DataFrame(X)

def run():
    data = get_dataset()
    
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

    return f_data
    

if __name__ == '__main__':
    result = run()

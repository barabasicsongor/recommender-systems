"""
Content based recommender system
Recommender system based on the description of the items.
Computes pairwise similarity score based on description, using TF-IDF vectors for each product.
"""
"""
Simple recommender system based on ratings.
This can be used when the user has not bought anything yet.
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


def get_dataset():
    X = [{'name': 'X-Man', 'vote_average': 7.7, 'vote_count': 5400, 'description': 'It is a really cool action movie'},
         {'name': 'Catwoman', 'vote_average': 8.1, 'vote_count': 10, 'description': 'The cat woman is always in action'},
         {'name': 'Wolf', 'vote_average': 6.5, 'vote_count': 200, 'description': 'The man is like a big cat'},
         {'name': 'Titanic', 'vote_average': 6.5, 'vote_count': 3200, 'description': 'This love story is hearbreaking and beautiful'},
         {'name': 'Honolulu', 'vote_average': 10, 'vote_count': 4, 'description': 'Really funny animation movie'}]

    return pd.DataFrame(X)


def prepare_data():
    data = get_dataset()

    # TF-IDF vectorizer
    tfidf = TfidfVectorizer(stop_words='english')

    # Fill NaN with empty string
    data['description'] = data['description'].fillna('')

    tfidf_matrix = tfidf.fit_transform(data['description'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    indices = pd.Series(data.index, index=data['name']).drop_duplicates()

    return data, indices, cosine_sim

def run(prod_name, nr_similars):
    data, indices, cosine_sim = prepare_data()
    idx = indices[prod_name]

    # Get the pairwsie similarity scores of all products with that product
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:nr_similars]
    
    prod_indices = [i[0] for i in sim_scores]

    return data['name'].iloc[prod_indices]



if __name__ == '__main__':
    result = run('Wolf', 3)
    print(result)

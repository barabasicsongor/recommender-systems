import pandas as pd
import numpy as np
from surprise import Reader, Dataset, SVD

def get_collab_recommendation(dataset, userid):
    
    dataframe = pd.DataFrame(dataset)
    reader = Reader(rating_scale=(1, 5))
    dataset = Dataset.load_from_df(dataframe[['userId','itemId','rating']], reader)
    trainset = dataset.build_full_trainset()

    algo = SVD()
    algo.train(trainset)

    user_ratings = np.zeros(trainset.n_items)
    
    for index, row in dataframe[dataframe['userId'] == userid].iterrows():
        user_ratings[row['itemId']] = row['rating']
    
    result = []
    for index, x in enumerate(user_ratings):
        if x == 0:
            prediction = algo.predict(userid, index)
            # Append (itemID, pred_rating)
            result.append((index, prediction.est))

    result.sort(key=lambda tup: tup[1], reverse=True)

    result = result[:2]
    result = [i for i,x in result]
    
    return result

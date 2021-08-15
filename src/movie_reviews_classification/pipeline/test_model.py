import os
from enum import Enum
from typing import Any, List
import pandas
from sklearn.feature_extraction.text import CountVectorizer

from movie_reviews_classification.pipeline.process_data import process_data


class ModelType(Enum):
    RANDOM_FOREST = 1


def test_model(model: Any, vectorizer: Any) -> None:
    '''Verifies model accuracy against test set'''

    # load test set
    base_path= os.getenv('BASE_PATH', '')
    path= f'{base_path}movie_reviews_classification/data/testData.tsv'
    test_set= pandas.read_csv(path, header=0, delimiter='\t', quoting=3)

    # clean test set
    cleaned_reviews= []
    for _, row in test_set.iterrows():
        review= process_data(row['review'])
        cleaned_reviews.append(review)

    # define test featurs
    test_data_features = vectorizer.transform(cleaned_reviews)
    test_data_features = test_data_features.toarray()

    # make and save test predictions
    results = model.predict(test_data_features)

    output = pandas.DataFrame(data={'id':test_set['id'], 'sentiment':results})
    output.to_csv('Bag_of_Words_model.csv', index=False, quoting=3)

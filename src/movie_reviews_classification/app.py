from movie_reviews_classification.pipeline.load_data import load_data
from movie_reviews_classification.pipeline.process_data import process_data
from movie_reviews_classification.pipeline.extract_features import extract_features
from movie_reviews_classification.pipeline.random_forest import random_forest
from movie_reviews_classification.pipeline.test_model import test_model


def run() -> None:
    '''Runs the sentiment analysis pipeline fo the bag of words project'''

    training_set = load_data('labeledTrainData.tsv')
    print(training_set)

    cleaned_reviews = []
    for _, row in training_set.iterrows():
        review = process_data(row['review'])
        cleaned_reviews.append(review)
    print(cleaned_reviews[0])

    features, vectorizer = extract_features(cleaned_reviews)

    model = random_forest(training_set['sentiment'], features)

    test_model(model, vectorizer)

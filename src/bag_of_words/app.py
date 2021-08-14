from bag_of_words.pipeline.load_data import load_data
from bag_of_words.pipeline.process_data import process_data


def run() -> None:
    '''Runs the sentiment analysis pipeline fo the bag of words project'''

    training_set = load_data('labeledTrainData.tsv')
    print(training_set)

    cleaned_reviews = []
    for _, row in training_set.iterrows():
        review = process_data(row['review'])
        cleaned_reviews.append(review)

    print(cleaned_reviews[0])

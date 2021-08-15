from typing import Any, List, Iterable, Tuple
from sklearn.feature_extraction.text import CountVectorizer


def extract_features(reviews: List[str]) -> Tuple[Iterable, Any]:
    '''Extract features - vector of unique words from a list of douments'''

    # initialize object for vectorization
    vectorizer = CountVectorizer(
        analyzer='word',
        tokenizer=None,
        preprocessor=None,
        stop_words=None,
        max_features=5000
    )

    # train vectorizer
    train_data_features = vectorizer.fit_transform(reviews)
    train_data_features = train_data_features.toarray()

    return train_data_features, vectorizer

from typing import Any, Iterable, List
from sklearn.ensemble import RandomForestClassifier


def random_forest(reviews: List[str], features: Iterable) -> Any:
    '''Classify reviews with a random forest model'''

    forest = RandomForestClassifier(n_estimators=100)
    forest = forest.fit(features, reviews)

    return forest
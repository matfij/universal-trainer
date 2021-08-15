import os
import re
from bs4 import BeautifulSoup


def process_data(span: str) -> str:
    '''Cleans text data a returns an array of words'''

    # remove html tags
    text = BeautifulSoup(span, 'html.parser').get_text()

    # remove non-alphanumeric characters
    text = re.sub('[^a-zA-Z0-9]', ' ', text)

    # convert to lower case, split into words
    words = text.lower().split()

    # remove stop words
    base_path = os.getenv('BASE_PATH', '')
    path = f'{base_path}movie_reviews_classification/data/stop_words.txt'

    with open(path, 'r') as file:
        content = file.read()
        stop_words = content.split(",")
    # covert to a set to enchance performance
    stop_words = set(stop_words)

    important_words = [word for word in words if not word in stop_words]

    # todo - porter stemming and lemmatizing

    return ' '.join(important_words)

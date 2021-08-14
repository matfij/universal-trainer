import os
import pandas
from pandas.core.frame import DataFrame


def load_data(data_file: str) -> DataFrame:
    '''Synchronously loads and returns data from a local file'''

    base_path = os.getenv('BASE_PATH', '')
    path = f'{base_path}bag_of_words/data/{data_file}'

    training_set = pandas.read_csv(path, header=0, delimiter='\t', quoting=3)

    return training_set

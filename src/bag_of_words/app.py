import os
from dotenv import load_dotenv
import pandas


def load_data():

    load_dotenv()
    base_path = os.getenv('BASE_PATH', '')
    path = base_path + 'bag_of_words/data/labeledTrainData.tsv'

    training_set = pandas.read_csv(path, header=0, delimiter='\t', quoting=3)
    print(training_set.shape)

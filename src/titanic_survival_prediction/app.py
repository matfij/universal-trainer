from titanic_survival_prediction.pipeline import data_processing as data
from titanic_survival_prediction.pipeline import model_training as train
from titanic_survival_prediction.pipeline import model_consuming as consume


def run():

    print('preparing data')
    training_set = data.prepare_training_data('/src/titanic_survival_prediction/data/train.csv')
    test_set = data.prepare_test_data('/src/titanic_survival_prediction/data/test.csv')

    print('training model')
    svm_model = train.train_svm(training_set)

    print('testing model')
    consume.test_svm(svm_model, test_set)

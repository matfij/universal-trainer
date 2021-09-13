from titanic_survival_prediction.pipeline.prepare_data import prepare_data
from titanic_survival_prediction.pipeline.train_model import train_model


def run():

    training_set, test_set = prepare_data()

    model = train_model(training_set)
    

    # choose model

    # train model

    # make predictions

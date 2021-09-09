def run():

    # load data
    import os
    import pandas
    from pandas.core.frame import DataFrame

    path = 'src/titanic_survival_prediction/data/train.csv'
    training_set = pandas.read_csv(path)

    # print((training_set['Age'].values[41]))
    # print(training_set.info())
    # print(training_set.describe())

    # explore features
    import matplotlib.pyplot as plt

    _, axs = plt.subplots(2, 2)
    axs[0, 0].hist(training_set['Age'])
    axs[0, 0].set_title('Age')
    axs[0, 1].hist(training_set['SibSp'].values)
    axs[0, 1].set_title('SibSp')
    axs[1, 0].hist(training_set['Parch'].values)
    axs[1, 0].set_title('Parch')
    axs[1, 1].hist(training_set['Fare'].values)
    axs[1, 1].set_title('Fare')
    plt.show()
    
    # clean data, remove features

    # choose model

    # train model

    # make predictions

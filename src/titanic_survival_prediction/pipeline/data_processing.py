from typing import Tuple
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


def prepare_training_data(path: str) -> pd.DataFrame:

    data = pd.read_csv(path)

    data['Sex'].replace({'male': 0, 'female': 1}, inplace=True)
    data['Embarked'].replace({'C': 1, 'Q': 2, 'S': 3}, inplace=True)
    data['Title'] = data['Name'].map(
        lambda x: x.split(',')[1].split('.')[0].strip()
    )

    _, axs_hist = plt.subplots(2, 2)
    axs_hist[0, 0].hist(data['Age'])
    axs_hist[0, 0].set_title('Age')
    axs_hist[0, 1].hist(data['SibSp'].values)
    axs_hist[0, 1].set_title('SibSp')
    axs_hist[1, 0].hist(data['Parch'].values)
    axs_hist[1, 0].set_title('Parch')
    axs_hist[1, 1].hist(data['Fare'].values)
    axs_hist[1, 1].set_title('Fare')
    _, axs_scat = plt.subplots(2, 2)
    axs_scat[0, 0].scatter(data['Survived'], data['Age'])
    axs_scat[0, 0].set_title('Age x Survived')
    axs_scat[0, 1].scatter(data['Survived'], data['Fare'])
    axs_scat[0, 1].set_title('Age x Fare')
    axs_scat[1, 0].scatter(data['Survived'], data['Embarked'])
    axs_scat[1, 0].set_title('Age x Embarked')
    plt.show()

    age_col_nulls = data['Age'].isnull()
    _ = age_col_nulls.where(age_col_nulls == True)

    print(
        pd.pivot_table(data, index='Survived', columns='Age', values='Sex', aggfunc ='count')
    )
    
    # clean data, remove features
    data['Age'] = data['Age'].fillna(data['Age'].mean())
    data['Fare'] = data['Fare'].fillna(data['Fare'].mean())

    training_data = pd.DataFrame({
        'Survived': [],
        'Pclass': [],
        'SibSp': [],
        'Parch': [],
        'Sex': [],
        'Age': [],
        'Title': [],
    })
    training_data['Survived'] = data['Survived']
    training_data['Pclass'] = data['Pclass']
    training_data['SibSp'] = data['SibSp']
    training_data['Parch'] = data['Parch']
    training_data['Sex'] = data['Sex']
    training_data['Age'] = data['Age']
    training_data['Title'] = data['Title']

    return training_data, training_data


def prepare_test_data() -> pd.DataFrame: 
    pass

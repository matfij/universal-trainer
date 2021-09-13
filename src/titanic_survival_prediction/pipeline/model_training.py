import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV


def train_svm(training_set: pd.DataFrame) -> SVC:

    x_train = training_set.drop(columns='Survived', axis=1)
    y_train = training_set['Survived']

    svc = SVC(probability=True)
    param_grid = [
        {'kernel': ['rbf'], 'gamma': [.1,.5,1,2,5,10], 'C': [.1, 1, 10, 100, 1000]},
        # {'kernel': ['linear'], 'C': [.1, 1, 10, 100, 1000]},
        # {'kernel': ['poly'], 'degree' : [2,3,4,5], 'C': [.1, 1, 10, 100, 1000]},
    ]
    clf_svc = GridSearchCV(svc, param_grid=param_grid, cv=5, verbose=True, n_jobs=-1)
    best_clf_svc = clf_svc.fit(x_train, y_train)

    return best_clf_svc

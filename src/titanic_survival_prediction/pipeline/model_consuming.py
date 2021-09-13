import pandas as pd
from sklearn.svm import SVC


def test_svm(svm: SVC, test_set: pd.DataFrame):
    results = svm.predict(test_set).astype(int)

    submission = {'PassengerId': list(range(892, 1310)), 'Survived': results}
    submission = pd.DataFrame(data=submission)
    submission.to_csv('base_submission.csv', index=False, quoting=3)

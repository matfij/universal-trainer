import sys
from dotenv import load_dotenv

from core.test import activation as activation_tests
from core.test import operations as operations_tests
# from titanic_survival_prediction import app as titanic_app
# from movie_reviews_classification import app as movie_app

load_dotenv()


activation_tests.run_activation_test()
operations_tests.run_operations_test()

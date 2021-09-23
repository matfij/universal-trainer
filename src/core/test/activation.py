from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from core.definitions import Placeholder, Variable

from core.graph import Graph
from core.session import Session
from core.operations import Add, MatMultiply, Sigmoid


def run_activation_test(verbose=False, plot=False):

    data = make_blobs(n_samples=50, n_features=2, centers=2)

    features = data[0]
    labels = data[1]

    if plot:
        plt.scatter(features[:, 0], features[:, 1], c=labels, cmap='coolwarm')
        plt.show()

    graph = Graph()
    graph.set_as_default()
    
    # separation line: y = wx + b
    x = Placeholder()
    w = Variable([1, 1])  
    b = Variable(-5)
    z = Add(MatMultiply(w, x), b)

    a = Sigmoid([z])

    session = Session()
    result_positive = session.run(operation=a, feed_dict={x: [8, 10]})
    result_negative = session.run(operation=a, feed_dict={x: [2, -10]})

    if verbose:
        print(result_positive, result_negative)

    assert result_positive > 0.9
    assert result_negative < 0.1

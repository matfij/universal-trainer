import numpy as np

from core.graph import Graph
from core.definitions import Placeholder, Variable
from core.operations import Multiply, Add, MatMultiply
from core.session import Session


def run_operations_test(verbose=False):
    graph = Graph()
    graph.set_as_default()

    A = Variable([[10, 20], [30,40]])
    B = Variable([[3, 2], [9, 7]])
    x = Placeholder()

    y = MatMultiply(A, x)
    z = Add(y, B)

    session = Session()
    result = session.run(operation=z, feed_dict={x:10})

    target = [[103, 202], [309, 407]]

    if verbose:
        print(result)

    assert np.array_equal(result, target)

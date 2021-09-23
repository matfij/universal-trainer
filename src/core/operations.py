from typing import List
import numpy as np

from core.graph import _default_graph


class Operation():
    '''Mathematical operation'''
    
    def __init__(self, input_nodes=[]) -> None:
        self.input_nodes = input_nodes
        self.output_nodes = []

        for node in input_nodes:
            node.output_nodes.append(self)

        _default_graph.operations.append(self)

    def compute(self):
        pass


class Add(Operation):

    def __init__(self, x, y) -> Operation:
        super().__init__([x, y])

    def compute(self, x, y):
        self.inputs = [x, y]
        return x + y


class Multiply(Operation):

    def __init__(self, x, y) -> Operation:
        super().__init__([x, y])

    def compute(self, x, y):
        self.inputs = [x, y]
        return x * y


class MatMultiply(Operation):

    def __init__(self, x, y) -> Operation:
        super().__init__([x, y])

    def compute(self, x, y):
        self.inputs = [x, y]
        return x.dot(y)


class Sigmoid(Operation):

    def __init__(self, input_nodes=...) -> Operation:
        super().__init__(input_nodes=input_nodes)

    def compute(self, x: List):
        return 1 / (1 + np.exp(-x))

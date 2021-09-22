class Operation:
    
    def __init__(self, input_nodes=[]) -> None:
        self.input_nodes = input_nodes
        self.output_nodes = []

        for node in input_nodes:
            node.output_nodes.append(self)

    def compute(self):
        pass


class Add(Operation):

    def __init__(self, x, y) -> None:
        super().__init__([x, y])

    def compute(self, x, y):
        self.inputs = [x, y]
        return x + y


class Multiply(Operation):

    def __init__(self, x, y) -> None:
        super().__init__([x, y])

    def compute(self, x, y):
        self.inputs = [x, y]
        return x * y


class MatMultiply(Operation):

    def __init__(self, x, y) -> None:
        super().__init__([x, y])

    def compute(self, x, y):
        self.inputs = [x, y]
        return x.dot(y)

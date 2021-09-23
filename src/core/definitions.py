from core.graph import _default_graph


class Placeholder:
    '''Empty node'''

    def __init__(self) -> None:
        self.output_nodes = []
        _default_graph.placeholder.append(self)


class Variable:
    '''Graph parameters'''

    def __init__(self, initial_value) -> None:
        self.output_nodes = []
        self.value = initial_value
        _default_graph.variables.append(self)
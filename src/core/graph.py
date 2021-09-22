class Graph:

    def __init__(self) -> None:
        self.operations = []
        self.placeholder = []
        self.variables = []

    def set_as_default(self):
        global _default_graph
        _default_graph = self


_default_graph = Graph()
_default_graph.set_as_default()

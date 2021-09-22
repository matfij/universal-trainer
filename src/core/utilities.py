from typing import Any
from operations import Operation


def traverser_postorder(operation: Operation):
    '''Post-order traversal of nodes.'''

    nodes_postorder = []
    def recurse(node):
        if isinstance(node, Operation):
            for input_node in node.input_nodes:
                recurse(input_node)
        nodes_postorder.append(node)

    recurse(operation)

    return nodes_postorder

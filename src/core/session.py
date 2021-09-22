import numpy as np

from operations import Operation
from definitions import Placeholder, Variable
from utilities import traverser_postorder


class Session():

    def run(self, operation: Operation, feed_dict={}):
        nodes_postorder = traverser_postorder(operation)

        for node in nodes_postorder:
            if isinstance(node, Placeholder):
                node.output = feed_dict[node]
            elif isinstance(node, Variable):
                node.output = node.value
            else: # Operation
                node.inputs = [input_node.output for input_node in node.input_nodes]
                node.output = node.compute(*node.inputs)

            if type(node.output) == list:
                node.output = np.array(node.output)

        return operation.output

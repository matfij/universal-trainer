from graph import Graph
from definitions import Placeholder, Variable
from operations import Multiply, Add, MatMultiply
from session import Session


graph = Graph()

A = Variable([[10, 20], [30,40]])
B = Variable([[3, 2], [9, 7]])
x = Placeholder()

y = MatMultiply(A, x)
z = Add(y, B)

session = Session()

result = session.run(operation=z, feed_dict={x:10})
print(result)

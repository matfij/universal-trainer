Perceptron - based ANN unit, composed of:
 - nucleus (body - activation function)
 - dendrites (weighted inputs - features, bias)
 - axon terminals (outputs - internal representation)

activation = sum of weighted inputs + bias

Basic ANN is composed of:
 - input layer (exposed to input features)
 - hidden layers (creates internal representation)
 - output layer (provides )

Activation functions:
 - unit step - non-differentiable
 - sign - non-differentiable
 - linear - differentiable
 - saturated linear - differentiable
 - logistic (sigmoid) - differentiable, decent performance
 - ReLU (rectified linear unit) - differentiable, fast to compute

Cost functions - evaluates neuron performance:
 - quadraic costs: C = sum(y-y')^2 / n; where: y - true value, y' - predicted value, n - number of smples, slow learning
 - cross entropy: C = (-1/n) sum(y ln(y') + (1-y) ln(1 - y')); allows for faster learning - the larger the difference, the more the neuron weights get adjusted

Gradient descend - minimizes error - a gradient (difference) is calculated for a given point of feature space (set of weights) and a step in direction that minimizes cost function (error) is taken.

Backpropagation - mechanism used to calculate the error contribution of each neuron after a batch of data is processed. It relies on the chain rule that makes partial calulations reusable that contributes to performance.

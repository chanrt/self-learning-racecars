from numpy import exp, random, zeros


class Layer:
    def __init__(self, num_inputs, num_neurons):
        self.weights = random.rand(num_neurons, num_inputs)
        self.biases = random.rand(num_neurons)
        
    def forward(self, inputs):
        return self.sigmoid(self.weights.dot(inputs) + self.biases)

    def sigmoid(self, x):
        return 1 / (1 + exp(-x))

    def relu(self, x):
        outputs = zeros(len(x))
        for i in range(len(x)):
            if x[i] > 0:
                outputs[i] = x[i]

        return outputs


class NeuralNetwork:
    def __init__(self, layers = None):
        self.layers = []

        if layers is not None:
            for i in range(len(layers) - 1):
                new_layer = Layer(layers[i], layers[i + 1])
                self.layers.append(new_layer)

    def set_layers(self, layers):
        self.layers = layers

    def predict(self, inputs):
        input_vector = inputs
        for layer in self.layers:
            input_vector = layer.forward(input_vector)
        return input_vector


if __name__ == '__main__':
    neural_network = NeuralNetwork([3, 4, 2])
    output = neural_network.forward([1, 2, 3])
    print(output)
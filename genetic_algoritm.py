from math import ceil
from random import choice, random

from car import Car
from neural_network import NeuralNetwork
from settings import settings as s


def recombine(parent1, parent2):
    nn1, nn2 = parent1.neural_network, parent2.neural_network
    num_layers = len(nn1.layers)
    result_layers = []

    for i in range(num_layers):
        if random() < 0.5:
            result_layers.append(nn1.layers[i])
        else:
            result_layers.append(nn2.layers[i])

    result_nn = NeuralNetwork()
    result_nn.set_layers(result_layers)

    new_car = Car()
    new_car.set_neural_network(result_nn)

    return new_car


def mutate(car):
    nn = car.neural_network
    num_layers = len(nn.layers)

    for i in range(num_layers):
        layer = nn.layers[i]
        num_neurons = len(layer.weights)
        num_inputs = len(layer.weights[0])

        for j in range(num_neurons):
            for k in range(num_inputs):
                if random() < s.mutation_rate:
                    layer.weights[j][k] += random() * s.mutation_range - s.mutation_range / 2

            if random() < s.mutation_rate:
                layer.biases[j] += random() * s.mutation_range - s.mutation_range / 2


def get_next_generation(cars):
    gene_pool = []

    for car in cars:
        fitness = car.distance_travelled ** 2
        gene_pool += [car.neural_network] * ceil(fitness)

    next_generation = []
    for _ in range(s.num_cars):
        child_nn = choice(gene_pool)
        child_car = Car()
        child_car.set_neural_network(child_nn)
        mutate(child_car)
        next_generation.append(child_car)

    return next_generation
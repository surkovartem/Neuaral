# Несколько входов: полный выполняемый вход (с использованием NumPy)

import numpy as np


def neuralNetwork(input, weights):
    pred = input.dot(weights)
    return pred


avrGameOfPlayer = np.array([8.5, 9.5, 9.9, 9.0])
wins = np.array([0.65, 0.8, 0.8, 0.9])
nFans = np.array([1.2, 1.3, 0.5, 1.0])
weights = np.array([0.1, 0.2, 0])

input = np.array([avrGameOfPlayer[0], wins[0], nFans[0]])
predication = neuralNetwork(input, weights)

print(predication)

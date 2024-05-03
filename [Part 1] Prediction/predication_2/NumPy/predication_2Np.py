# Прогнозирование с несколькими выходами (с использованием NumPy)

import numpy as np


# Нейронная сеть
def neuralNetwork(input, weights):
    pred = input.dot(weights)
    return pred


wins = np.array([0.65, 0.8, 0.8, 0.9])
weights = np.array([0.3, 0.2, 0.9])

input = np.array(wins[0])
predication = neuralNetwork(input, weights)
print(f"Вероятность травмы: {predication[0]} \n"
      f"Вероятность победы: {predication[1]} \n"
      f"Вероятность поражения: {predication[2]}")

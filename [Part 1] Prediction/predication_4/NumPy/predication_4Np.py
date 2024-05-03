# Пронозирование на основе прогнозов (с использованием NumPy)

import numpy as np


# Нейронная сеть
def neuralNetwork(input, weights):
    # Получение скрытого слоя
    hid = input.dot(weights[0])
    pred = hid.dot(weights[1])
    return pred


weights1 = np.array([[0.1, 0.2, -0.1],
                     [-0.1, 0.1, 0.9],
                     [0.1, 0.4, 0.1]]).T

weights2 = np.array([[0.3, 1.1, -0.3],
                     [0.1, 0.2, 0.0],
                     [0.0, 1.3, 0.1]]).T

# Веса
weights = [weights1, weights2]
# текущее среднее число игр
avrGameOfPlayer = np.array([8.5, 9.5, 9.9, 9.0])
# текущая доля игр, окончившихся победой (процент)
wins = np.array([0.65, 0.8, 0.8, 0, 9])
# число болельщиков (в миллионах)
nFans = np.array([1.2, 1.3, 0.5, 1.0])

input = np.array([avrGameOfPlayer[0], wins[0], nFans[0]])
prediction = neuralNetwork(input, weights)
print(f"Вероятность травмы: {prediction[0]} \n"
      f"Вероятность победы: {prediction[1]} \n"
      f"Вероятность поражения: {prediction[2]}")

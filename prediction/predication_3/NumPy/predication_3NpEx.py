# Прогнозирование с несколькимим входами и выходами (с использованием NumPy и для всех 4х случаев игр)

import numpy as np


# Нейронная сеть
def neuralNetwork(input, weights):
    pred = input.dot(weights)
    return pred


# веса
weights = np.array([[0.1, 0.1, -0.3],
                    [0.1, 0.2, 0.0],
                    [0.0, 1.3, 0.1]]).T
# текущее среднее число игр
avrGameOfPlayer = np.array([8.5, 9.5, 9.9, 9.0])
# текущая доля игр, окончившихся победой (процент)
wins = np.array([0.65, 0.8, 0.8, 0, 9])
# число болельщиков (в миллионах)
nFans = np.array([1.2, 1.3, 0.5, 1.0])

for i in range(4):
    input = np.array([avrGameOfPlayer[i], wins[i], nFans[i]])
    prediction = neuralNetwork(input, weights)
    print(f"Игра: {i + 1} \n"
          f"Вероятность травмы: {prediction[0]} \n"
          f"Вероятность победы: {prediction[1]} \n"
          f"Вероятность поражения: {prediction[2]}\n")

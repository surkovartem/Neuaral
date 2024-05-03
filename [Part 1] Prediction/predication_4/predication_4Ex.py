# Пронозирование на основе прогнозов (для всех 4х случаев игр)

# Нейронная сеть
def neuralNetwork(input, weights):
    # Получение скрытого слоя
    hid = vecMatMultiplication(input, weights[0])
    pred = vecMatMultiplication(hid, weights[1])
    return pred


# Обход всех векторов весов и вычисление прогноза с помощью метода wSum
def vecMatMultiplication(input, weights):
    assert (len(input) == len(weights))
    output = [0, 0, 0]
    for i in range(len(input)):
        output[i] = wSum(input, weights[i])
    return output


# Получение взвешенной суммы (скалярное произведение)
def wSum(input, weights):
    assert len(input) == len(weights)
    output = 0
    for i in range(len(input)):
        output += (input[i] * weights[i])
    return output


weights1 = [[0.1, 0.2, -0.1],
            [-0.1, 0.1, 0.9],
            [0.1, 0.4, 0.1]]

weights2 = [[0.3, 1.1, -0.3],
            [0.1, 0.2, 0.0],
            [0.0, 1.3, 0.1]]

# Веса
weights = [weights1, weights2]
# текущее среднее число игр
avrGameOfPlayer = [8.5, 9.5, 9.9, 9.0]
# текущая доля игр, окончившихся победой (процент)
wins = [0.65, 0.8, 0.8, 0, 9]
# число болельщиков (в миллионах)
nFans = [1.2, 1.3, 0.5, 1.0]

input = [avrGameOfPlayer, wins, nFans]

for i in range(4):
    input = [avrGameOfPlayer[i], wins[i], nFans[i]]
    prediction = neuralNetwork(input, weights)
    print(f"Игра: {i + 1} \n"
          f"Вероятность травмы: {prediction[0]} \n"
          f"Вероятность победы: {prediction[1]} \n"
          f"Вероятность поражения: {prediction[2]} \n")

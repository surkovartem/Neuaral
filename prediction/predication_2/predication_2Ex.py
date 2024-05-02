# Прогнозирование с несколькими выходами (для всех 4х случаев игр)

# Нейронная сеть
def neuralNetwork(input, weighs):
    pred = elemMultiplication(input, weighs)
    return pred


# Обход вектора весов и вычисление прогноза победы
def elemMultiplication(num, vector):
    output = [0, 0, 0]
    assert (len(output) == len(vector))
    for i in range(len(vector)):
        output[i] = num * vector[i]
    return output


wins = [0.65, 0.8, 0.8, 0.9]
weights = [0.3, 0.2, 0.9]

for i in range(4):
    input = wins[i]
    predication = neuralNetwork(input, weights)
    print(f"Игра: {i + 1} \n"
          f"Вероятность травмы: {predication[0]} \n"
          f"Вероятность победы: {predication[1]} \n"
          f"Вероятность поражения: {predication[2]}\n")

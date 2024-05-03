# Несколько входов: полный выполняемый вход

# Нейронная сеть, вычисляющая прогноз победы, с помощью метода wSum()
def neural_network(input, weights):
    pred = wSum(input, weights)
    return pred


# Получение взвешенной суммы (скалярное произведение)
def wSum(a, b):
    assert (len(a) == len(b))
    output = 0
    for i in range(len(a)):
        output += a[i] * b[i]
    # output = взвешенная сумма входов (взвешенная сумма или скалярное произведение)
    return output


# текущее среднее число игр, сыгранных игроками
avrGameOfPlayer = [8.5, 9.5, 9.9, 9.0]
# текущая доля игр, окончившихся победой (процент)
wins = [0.65, 0.8, 0.8, 0, 9]
# число болельщиков (в миллионах)
nFans = [1.2, 1.3, 0.5, 1.0]
# веса
weights = [0.1, 0.2, 0]

input = [avrGameOfPlayer[0], wins[0], nFans[0]]
predication = neural_network(input, weights)
print(f"Вероятность победы: {predication}")

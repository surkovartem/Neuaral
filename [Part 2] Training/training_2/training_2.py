'''
Обучение методом "Горячо-Холодно" - не эффективно, в силу того,
что прогноз вычисляется несколько раз для корректировки веса.

Далее представлен подход вычисления направления и величины из ошибки.
Данный подход называется "Градиентный спуск"
'''


# Получение предсказания
def getPredication(input, weight):
    return input * weight


# Вычисление ошибки
def getError(prediction, targetPredication):
    return (prediction - targetPredication) ** 2


# DIRECTION_AND_AMOUNT - как должен изменитья вес.
# Три принципа: остановка, обращение знака, масштабирование.
def getDirectionAndAmount(prediction, targetPredication, input):
    return (prediction - targetPredication) * input


input = 0.5
weight = 0.5
targetPredication = 0.8

for i in range(20):
    predication = getPredication(input, weight)
    error = getError(predication, targetPredication)
    weight = weight - getDirectionAndAmount(predication, targetPredication, input)
    print(f"itter = {i}, input = {input}, weight = {weight}, predication = {predication}, error = {error}")

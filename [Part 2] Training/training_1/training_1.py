'''
Обучение нейронной сети, методом "Горячо-холодно"
'''


# Метод получения предсказания
def getPrediction(input, weight):
    return input * weight


# Метод получения ошибки
def getError(prediction, target):
    return (target - prediction) ** 2


# Метод корректировки веса
def correctWeight(weight, downError, upError, step):
    if downError < upError:
        return weight - step
    if downError > upError:
        return weight + step


# входные данные
input = 0.5
# вес
weight = 0.5
# целевое предсказание
target = 0.8
# шаг корректировки веса
step = 0.001
prediction = 0
itterations = 1

while (prediction < target):
    # Получаем предсказание
    prediction = getPrediction(input, weight)
    error = getError(prediction, target)
    print(f"Иттерация = {itterations}, input = {input}, weight = {weight}, predication = {prediction}, error = {error}")

    # Предсказание с деинкрементным весом
    downPredication = getPrediction(input, weight - step)
    downError = getError(downPredication, target)

    # Предсказание с инкрементным весом
    upPredication = getPrediction(input, weight + step)
    upError = getError(upPredication, target)

    # Новое значение веса
    weight = correctWeight(weight, downError, upError, step)
    itterations += 1

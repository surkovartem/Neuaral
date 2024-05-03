def neuralNetwork(input, weight):
    return input * weight


def getError(predication, goal):
    return (predication - goal) ** 2


avrGameOfPlayer = [8.5]
winOrLoseBinary = [1]
input = avrGameOfPlayer[0]
weight = 0.1
true = winOrLoseBinary[0]
step = 0.01

prediction = neuralNetwork(input, weight)
error = getError(prediction, true)
print(f"Вероятность победы: {prediction}")
print(f"Ошибка: {error}\n")

predictionCorrectWeightUp = neuralNetwork(input, weight) + step
errorUp = getError(predictionCorrectWeightUp, true)
print(f"Ошибка при приросте веса: {errorUp}")

predictionCorrectWeightDown = neuralNetwork(input, weight) - step
errorDown = getError(predictionCorrectWeightDown, true)
print(f"Ошибка при уменьшение веса: {errorDown}")

if((error > errorDown) or (error > errorUp)):
    if(errorDown < errorUp):
        weight -= step
    if(errorUp < errorDown):
        weight += step

print(f"Новое значение веса: {weight}\n")

prediction = neuralNetwork(input, weight)
print(f"Вероятность победы: {prediction}")
print(f"Ошибка: {getError(prediction, true)}")

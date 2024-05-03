def neuralNetwork(input, weight):
    return input * weight


def getError(prediction, goal):
    return (prediction - goal) ** 2


input = 0.5
weight = 0.5
goalPredication = 0.8

predication = neuralNetwork(input, weight)
error = getError(predication, goalPredication)

print(f"input: {input}\n"
      f"weight: {weight}\n"
      f"predication: {predication}\n"
      f"goal: {goalPredication}\n"
      f"Ошибка равна: {error}\n")

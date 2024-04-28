# Прогнозирование с несколькими выходами

def elemMultiplication(num, vector):
    output = [0, 0, 0]
    assert (len(output) == len(vector))
    for i in range(len(vector)):
        output[i] = num * vector[i]
    return output


def neuralNetwork(input, weighs):
    pred = elemMultiplication(input, weighs)
    return pred


weights = [0.3, 0.2, 0.9]
wins = [0.65, 0.8, 0.8, 0.9]
input = wins[0]
pred = neuralNetwork(input, weights)
print(pred)

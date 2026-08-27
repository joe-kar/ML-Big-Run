import random

class multilin:
    def __init__(self, points, outs):
        self.xs = [i + [1] for i in points]
        self.ys = outs
        self.weights = [random.randint(-10, 10) for _ in range(len(points[0]) + 1)]
        self.alpha = 0.05

    #calculates one output based on one set of inputs
    def calculate(self, x1s):
        if len(x1s) == len(self.weights) - 1:
            x1s.append(1)
        y = sum([x1s[i] * self.weights[i] for i in range(len(x1s))])
        return y

    #calculates the mean squared error
    def MSE(self, yhats):
        return sum([(self.ys[i] - yhats[i])**2 for i in range(len(self.ys))]) / len(yhats)

    #updates all weights by one step
    def update(self):
        weight_diffs = []
        for i in range(len(self.weights)):
            weight_diffs.append(self.alpha * (2/len(self.xs)) * sum([(self.ys[j] - self.calculate(self.xs[j])) * self.xs[j][i] for j in range(len(self.ys))]))
        for i in range(len(weight_diffs)):
            self.weights[i] += weight_diffs[i]

if __name__ == "__main__":
    dummy = [[1, 2], [3, 4]]
    dummy_out = [6, 9]
    model = multilin(dummy, dummy_out)
    print(model.weights)
    print(model.calculate(dummy[0]))
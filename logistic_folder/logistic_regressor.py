import random
import math

class logistic_regression():
    def __init__(self, xs, ys):
        self.xs = [i + [1] for i in xs]
        self.ys = ys
        self.weights = [1 for _ in range(len(self.xs[0]))]
        self.alpha = 0.01

    def calculate(self, feature_list):
        z = sum([feature_list[i] * self.weights[i] for i in range(len(self.weights))])
        if z > 0:
            return 1/(1 + math.exp(-z))
        else:
            return math.exp(z)/(1 + math.exp(z))

    def error(self, yhat, y):
        if yhat == 0:
            yhat = 0.000000000000001
        if yhat == 1:
            yhat = 0.999999999999999
        return y*math.log(yhat) + (1-y)*(math.log(1-yhat))

    def update(self, feature_list, y, yhat):
        for i in range(len(self.weights)):
            self.weights[i] += feature_list[i] * (y - yhat) * self.alpha

    def train(self, runs=1000):
        print(f"Starting weights: {self.weights} Guess: {self.calculate(self.xs[0])} Actual: {self.ys[0]}")
        for run in range(runs):
            for i in range(len(self.xs)):
                yhat = self.calculate(self.xs[i])
                y = self.ys[i]
                self.update(self.xs[i], y, yhat)
            if run % 100 == 0:
                choices = [random.randint(0, len(self.ys) - 1) for _ in range(10)]
                predictions = [self.calculate(self.xs[mu]) for mu in choices]
                error_avg = sum([self.error(predictions[tau], self.ys[choices[tau]]) for tau in range(10)])/10
                print(f"Run: {run + 1} Guess: {self.calculate(self.xs[0])} Actual: {self.ys[0]} Average error across 10 random guess: {error_avg}")
                print(self.weights)
        print("Training Complete")

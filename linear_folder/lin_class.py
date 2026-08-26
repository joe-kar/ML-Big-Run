import random

class LinClass:
    def __init__(self, alpha = 0.0001, w1 = random.randint(-10, 10), w0 = random.randint(-10, 10)):
        self.w1 = w1
        self.w0 = w0
        self.alpha = alpha

    #perform one calc
    def calculate(self, x):
        return self.w1 * x + self.w0

    #calculates the mean squared error
    def MSE(self, points):
        residuals = []
        for i, j in points:
            y_hat = self.calculate(i)
            residuals.append((j - y_hat)**2)
        return sum(residuals)/len(residuals)

    #takes a list of points and performs one update to weights
    def update(self, points):
        residuals_0 = []
        residuals_1 = []
        for i, j in points:
            y_hat = self.calculate(i)
            residuals_0.append(j - y_hat)
            residuals_1.append((j - y_hat) * i)
        self.w0 += 2 * self.alpha * sum(residuals_0)/len(points)
        self.w1 += 2 * self.alpha * sum(residuals_1)/len(points)

    #check if model is live
    def working_class(self):
        print("Sieze the means of production!")
import random
import math

def main():
    actual_weights, xs, ys = generate_data()

#here we generate data for the model to train on
#we imagine that the factors are contributing to heart disease
def generate_data():
    #the weights are how much each factor contributes to the condition
    #negative weights are factors like exercise which decreases heart disease risk
    #positive weights are like hours spent sedentary which increases heart disease risk
    real_weights = [random.randint(-10, 10) for _ in range(random.randint(1, 10))]
    #each row is a person, and the column is how much of the factor that person does/is/has
    xs = [[random.randint(-10, 10) for _ in range(len(real_weights) - 1)] for _ in range(random.randint(100, 200))]
    #using this we calculate the probability by taking the logistic of the dot product
    zs = [sum([j[i] * real_weights[i] for i in range(len(j))]) + real_weights[-1] for j in xs]
    ys = [1 if 1/(1+math.exp(i)) > 0.5 else 0 for i in zs]
    return real_weights, xs, ys

#splits data into training and testing
def split_data(rawxs, rawys):
    pass

#normalizes data
def normalize_data(xs):
    pass

if __name__ == "__main__":
    main()
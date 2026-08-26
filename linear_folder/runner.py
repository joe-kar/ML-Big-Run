import random
from lin_class import LinClass

def main(message = "yeet"):
    print(message)
    data = generate_points()
    feed = normalize(data[0])
    #instantiate model
    model = LinClass()
    model.working_class()
    #check weights vs real m and c
    print(f"Real Weights: {data[1]}")
    print(f"Model Weights: {[model.w1, model.w0]}")
    #split data 90/10
    training_data = feed[:90]
    testing_data = feed[90:]
    #Run updates
    for i in range(1000):
        model.update(training_data)
        if (i + 1) % 100 == 0:
            print(f"Round {i + 1}: MSE = {model.MSE(testing_data)}")
        if model.MSE(testing_data) < 1e-10:
            print(f"Cutting training short at update {i}, cos we are done")
            break
    #Testing time
    for i in testing_data:
        print(f"Guess = {model.calculate(i[0])}, Actual = {i[1]}")
    print("Final MSE: " + str(model.MSE(testing_data)) + "\nFinal weights: " + str([model.w1, model.w0]) + "\nActual Weights: " + str(data[1]))

#Here we create a random set of points that the model will try to fit
def generate_points():
    m = random.randint(-10, 10)
    c = random.randint(-10, 10)
    points = []
    while len(points) < 100:
        x = random.randint(-100, 100)
        points.append((x, x * m + c))
    return (points, [m, c])

#normalize the input points just for practice
def normalize(points):
    xs = [i for i, j in points]
    mean = sum(xs)/len(xs)
    stdev = (sum([(j - mean)**2 for j in xs])/len(xs))**0.5
    normalized = [(k - mean)/stdev for k in xs]
    return list(zip(normalized, [l for m, l in points]))

if __name__ == "__main__":
    main()
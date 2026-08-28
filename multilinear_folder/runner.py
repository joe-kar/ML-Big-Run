import random
import csv
from multilin_class import multilin

def main(): 
    row_names = ["Cement", "Blast Furnace Slag", "Fly Ash", "Water", "Superplasticizer", "Coarse Aggregate", "Fine Aggregate", "Age"]
    y_name = "Strength"
    unsanitized_xs, ys = read_in_data("concrete_data.csv", row_names, y_name)
    #actual_line = generate_line()
    #unsanitized_xs, ys = generate_points(actual_line)
    training_x_unsatized, training_y, testing_x_unsanitized, testing_y = split(unsanitized_xs, ys)
    training_x_sanitized, means, stdevs = normalize(training_x_unsatized)
    testing_x_sanitized = normalize_known(testing_x_unsanitized, means, stdevs)
    model = multilin(training_x_sanitized, training_y)
    temp_yhats = [model.calculate(j) for j in training_x_sanitized]
    print(f"Guess: {model.calculate(testing_x_sanitized[0] + [1])} Actual: {testing_y[0]}, MSE: {model.MSE(temp_yhats)}")
    for i in range(10000):
        model.update()
        if (i + 1) % 100 == 0:
            temp_yhats = [model.calculate(j) for j in training_x_sanitized]
            print(f"Run {i + 1}: MSE = {model.MSE(temp_yhats)}")
            print(f"Guess: {model.calculate(testing_x_sanitized[0] + [1])} Actual: {testing_y[0]}")
    for i, j in enumerate(testing_x_sanitized):
        print(f"Guess: {model.calculate(j + [1])} Actual: {testing_y[i]}")

#here we shall generate a line
def generate_line():
    inputs = []
    for _ in range(random.randint(1, 10)):
        inputs.append((random.random() - 0.5) * 20)
    #returns [b1, b2, ... , bn] where bn is the c
    return inputs

#here we shall generate the points from the line
def generate_points(line):
    xs = []
    ys = []
    #do 100 random points
    while len(ys) < 100:
        x = [random.randint(-100, 100) for _ in range(len(line) - 1)]
        y = sum([x[i] * line[i] for i in range(len(x))]) + line[-1] #dot product
        xs.append(x)
        ys.append(y)
    #returns [[x1, x2, ... xn]... ], [y1, y2, ..., yn]
    return xs, ys

#i got a ticket for the long way round
def normalize(xs):
    xs_inverse = [[] for _ in range(len(xs[0]))]
    #flip the matrix
    for i in xs:
        for j, k in enumerate(i):
            xs_inverse[j].append(k)
    #simple means function
    means = [sum(i)/len(i) for i in xs_inverse]
    stdevs = []
    #standard deviation function
    for count, feature_list in enumerate(xs_inverse):
        stdevs.append((sum([(item - means[count])**2 for item in feature_list])/len(feature_list)) ** 0.5)
    #create normalized values
    xs_pro = []
    for i in xs:
        temp = []
        for j, k in enumerate(i):
            temp.append((k - means[j])/stdevs[j])
        xs_pro.append(temp)
    return xs_pro, means, stdevs

#normalize data according to the training data
def normalize_known(xs, means, stdevs):
    xs_pro = []
    for i in xs:
        temp = []
        for j, k in enumerate(i):
            temp.append((k - means[j])/stdevs[j])
        xs_pro.append(temp)
    return xs_pro

#splits data into training data and testing data
def split(xs, ys):
    training_x = []
    training_y = []
    testing_x = []
    testing_y = []
    for i, j in enumerate(xs):
        if random.randint(1, 10) == 6:
            testing_x.append(j)
            testing_y.append(ys[i])
        else:
            training_x.append(j)
            training_y.append(ys[i])
    return training_x, training_y, testing_x, testing_y

def read_in_data(csv_name, row_names, y_name):
    with open(csv_name, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        xs = []
        ys = []
        for row in reader:
            temp = [float(row[i]) for i in row_names]
            xs.append(temp)
            ys.append(float(row[y_name]))
        return xs, ys

if __name__ == "__main__":
    main()
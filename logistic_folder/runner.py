import random
import math

def main():
    actual_weights, xs, ys = generate_data()
    training_unsanitized_x, training_y, testing_unsanitized_x, testing_y = split_data(xs, ys)
    training_sanitized_x, means, stdevs = normalize(training_unsanitized_x)
    testing_sanitized_x = normalize(testing_unsanitized_x, means, stdevs)

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
    training_x = []
    testing_x = []
    training_y = []
    testing_y = []
    for i in range(len(rawxs)):
        if random.random() <= 0.1:
            testing_x.append(rawxs[i])
            testing_y.append(rawys[i])
        else:
            training_x.append(rawxs[i])
            training_y.append(rawys[i])
    return training_x, training_y, testing_x, testing_y

#normalizes data
def normalize(xs, means=None, stdevs=None):
    if means == None:
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

if __name__ == "__main__":
    main()
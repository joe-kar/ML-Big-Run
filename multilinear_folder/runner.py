import random

def main():
    actual_line = generate_line()
    unsanitized_xs, ys = generate_points(actual_line)
    sanitized_xs = normalize(unsanitized_xs)
    print("--------------------------------------------")
    print(sanitized_xs)
    print("--------------------------------------------")
    print(unsanitized_xs)

#here we shall generate a line
def generate_line():
    inputs = []
    for _ in range(random.randint(1, 10)):
        inputs.append((random.random() - 0.5) * 20)
    #returns [b1, b2, ... , bn]
    return inputs

#here we shall generate the points from the line
def generate_points(line):
    xs = []
    ys = []
    #do 100 random points
    while len(ys) < 100:
        x = [random.randint(-100, 100) for _ in range(len(line))]
        y = sum([x[i] * line[i] for i in range(len(line))]) #dot product
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
    return xs_pro

if __name__ == "__main__":
    main()
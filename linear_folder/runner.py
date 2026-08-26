import random
from lin_class import LinClass

def main(message = "yeet"):
    print(message)
    data = generate_points()
    model = LinClass()
    model.working_class()
    print(model.w1)
    print(model.w2)    

#Here we create a random set of points that the model will try to fit
def generate_points():
    m = random.randint(-10, 10)
    c = random.randint(-10, 10)
    points = []
    while len(points) < 100:
        x = random.randint(-100, 100)
        points.append((x, x * m + c))
    return (points, [m, c])


if __name__ == "__main__":
    main()
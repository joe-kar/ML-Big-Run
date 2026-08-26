import random

def main(message = "yeet"):
    print(message)

def generate_points():
    m = random.randint(-10, 10)
    c = random.randint(-10, 10)
    points = []
    for i in range(100):
        x = random.randint(-100, 100)
        points.append((x, x * m + c))
    return (points, [m, c])


if __name__ == "__main__":
    main()
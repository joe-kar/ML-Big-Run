import random

def main(message = "yeet"):
    print(message)
    data = generate_points()
    print(data)
    for count, i in enumerate(data[0]):
        if random.randint(1, 10) == 1:
            print(f"Halt! Point {count + 1} you have been selected for a random inspection: {i[0]} x {data[1][0]} + {data[1][1]} = {i[1]}")

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
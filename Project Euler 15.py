import time
start = time.time()


def lattice(side_length):  # assumes the lattice is a square
    numerator = 1
    denominator = 1

    for i in range(side_length, side_length * 2):  # used to calculate the top factorial
        numerator = numerator * i

    for i in range(2, side_length):
        denominator = denominator * i

    paths = (numerator / denominator)
    print(paths)


lattice(20)

end = time.time()
print(end - start)
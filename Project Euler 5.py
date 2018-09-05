x = 20
while True:
    for i in range(1,20):
        if x % i != 0:
            x += 20
            print(x)
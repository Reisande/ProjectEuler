def reverse_func(z):
    for i in range(1, z):
        reverse = str(z)[::-1]
        return int(reverse)

for x in range(1, 1000):
    for y in range(1,1000):
        if reverse_func(x*y) == x*y:
            print(x * y)
              if x*y >= z:
                z = x*y
print(z)

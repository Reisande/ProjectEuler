z = int(input("enter number which you want prime factorization of: "))
def is_prime(x):
    if x >= 2:
        for y in range(2, x):
            if x % y == 0:
                return False
    print(i)
for i in range(1, z):
    if z % i == 0:
        is_prime(i)
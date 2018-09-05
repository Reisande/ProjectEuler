import time
start = time.time()


def primes_finder(n):
    primes_list = []
    prime = 2
    while len(primes_list) != n:
        prime = prime + 1
        if is_prime(prime) == False:
            continue
        else:
            primes_list.append(prime)
    print(primes_list[-1])


def is_prime(x):
    if x > 2:
        for y in range(2, x):
            if x % y == 0:
                return False
    elif x == 2:
        return True


primes_finder(10000)

end = time.time()
print(end - start)
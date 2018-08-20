import time
start = time.time()

def sieve(n): #this only work for numbers less than n, if you want to change it to sum first n terms, change num in ln 7 to len(primes_list)
    primes_list = [2, 3]
    num = 4
    while num < n:
        num_sqrt = int(num ** .5)
        num += 1
        for x in range(0, num_sqrt):
            if num % primes_list[x] == 0:
                break
            elif primes_list[x] > num_sqrt:
                primes_list.append(num)
                break
    #print(primes_list[-1])
    print(primes_list)
sieve(2000000)

end = time.time()
print(end - start)
import time
start_time = time.time()


def divisors(divisors_check):
    root = int(divisors_check**.5) + 1
    divisors_list = [1, divisors_check]
    for i in range(2, root):
        if divisors_check % i == 0:
            inverse = divisors_check / i
            divisors_list.append(i)
            divisors_list.append(inverse)
    return divisors_list  #check with is_prime/ eratosthenes_sieve


def triangle():
    triangle_number = 0
    triangle_number_list = [0, 1, 3]
    while len(divisors(triangle_number_list[-1])) < 500:
        triangle_number = 2*triangle_number_list[-1] - triangle_number_list[-2] + 1
        triangle_number_list.append(triangle_number)
    print(triangle_number)

triangle()

end_time = time.time()
print(end_time - start_time)
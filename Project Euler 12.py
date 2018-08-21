import time
start_time = time.time()


def divisors(divisors_check):
    root = int(divisors_check**.5) + 1
    divisors_list = [(number, divisors_check/number) for number in range(1, root) if divisors_check % number == 0]
    return len(divisors_list)*2


def triangle():
    triangle_number = 0
    triangle_number_list = [0, 1, 3]
    while divisors(triangle_number_list[-1]) < 500:
        triangle_number = 2*triangle_number_list[-1] - triangle_number_list[-2] + 1
        triangle_number_list.append(triangle_number)
    print(triangle_number)


triangle()

end_time = time.time()
print(end_time - start_time)
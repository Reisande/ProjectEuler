def divisor_check(input_number):
    divisors_list = [1]
    for divisor in range(2, int(input_number ** .5 + 1)):
        if input_number % divisor == 0:
            reciprocal = input_number // divisor
            divisors_list.append(divisor)
            divisors_list.append(reciprocal)
    return divisors_list  # returns an unsorted list, but order doesnt matter because sum is only important factor


def amicability(input_number):  # finds amicability by comparing the sum of divisors twice
    number_couple = sum(divisor_check(input_number))
    if sum(divisor_check(number_couple)) == input_number:
        if number_couple != input_number:  # this line is to exclude any perfect numbers, as they are not amicable
            return input_number


amicable_number_list = []
for i in range(1, 10000):
    if type(amicability(i)) == int:
        amicable_number_list.append(amicability(i))

print(amicable_number_list)
print(sum(amicable_number_list))

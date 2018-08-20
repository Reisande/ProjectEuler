def collatz_sequence(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
    return sequence


max_len = 1
for i in range(1, 1000):
    if len(collatz_sequence(i)) > max_len:
        max_len = len(collatz_sequence(i))
        print(i, max_len)
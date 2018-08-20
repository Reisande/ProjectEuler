big_num = 1
for i in range(100, 1, -1):
    big_num = i * big_num
big_num = str(big_num)
big_num = list(map(int, big_num))
print(sum(big_num))
def sum_of_squares(n):
    square = 0
    for i in range(1, n+1):
        square = square + i**2
    return square
    ## square is going to be the squared number, sum is going to be the sum of squares, the end goal is to find sum-square of n
def square_of_sums(n):
    sum = 0
    for i in range(1, n +1):
        sum = sum + i
    return (sum**2)
number = int(input())
print(str(square_of_sums(number)-sum_of_squares(number)))
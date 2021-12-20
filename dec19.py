# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0

number = 10
def solution(number):
    sum = 0
    for i in range(1, number):
        if(i % 3 == 0) & (i % 5 == 0):
            sum += (i)
        elif (i % 3 == 0) | (i % 5 == 0):
            sum += (i)        
    return sum
print(solution(number))

# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

# Examples:
# Input: 42145 Output: 54421
# Input: 145263 Output: 654321
# Input: 123456789 Output: 987654321

def descending_order(num):

    return int("".join(map(str, sorted([i for i in str(num)], reverse=True))))
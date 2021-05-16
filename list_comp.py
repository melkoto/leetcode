# Решение https://youtu.be/oBhqArvkcPY
# Sum of positive
# https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python
def positive_sum(arr):
    return sum(x for x in arr if x > 0)


# Find numbers which are divisible by given number
# https://www.codewars.com/kata/55edaba99da3a9c84000003b/train/python
def divisible_by(numbers, divisor):
    return [num for num in numbers if num % divisor == 0]


# Square(n) Sum
# https://www.codewars.com/kata/515e271a311df0350d00000f/train/python
def square_sum(numbers):
    return sum(num ** 2 for num in numbers)


# Convert an array of strings to array of numbers
# https://www.codewars.com/kata/5783d8f3202c0e486c001d23/train/python
def to_float_array(arr):
    # your code here
    return [int(num) if type(num) is int else float(num) for num in arr]

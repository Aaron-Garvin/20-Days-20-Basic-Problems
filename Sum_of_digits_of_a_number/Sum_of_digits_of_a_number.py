#python program for finding the sum of digits of a number 

# Method 1 : (Using While loop)

num1 = int(input("Enter a number : "))
sum_digits1 = 0

while num1 > 0:
    sum_digits1 += num1 % 10    # Store the last variable in sum_digits1
    num1 = num1 // 10           # Last digits is removed from the number

print("Sum of digits:", sum_digits1)


# Method 2 : (Using For Loop)

num2 = input("Enter a number : ")
sum_digits2 = 0

for digit in num2:
    sum_digits2 += int(digit)

print("Sum of digits:", sum_digits2)


# Method 3 : (List Comprehention)

num3 = input("Enter a number : ")
sum_digits3 = sum([int(digit) for digit in num3])

print("Sum of digits:", sum_digits3)


# Method 4 : (Using map() function)

num4 = input("Enter a number: ")         # Example: "1234"
sum_digits4 = sum(map(int, num4))        # map(int, num) → [1, 2, 3, 4]

# map(function, iterable) applies a function to each item in an iterable (like a list or string).
# The outer sum() will sum up all the values 

print("Sum of digits:", sum_digits4)


# Method 5 : (Using function)

def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

num = int(input("Enter a number: "))
print("Sum of digits:", sum_digits(num))


# Method 6 : (Using recursion)

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)

num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(num))

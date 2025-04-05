# Method 1 : (Using function)

def count_even_odd(numbers):
    even_count = 0
    odd_count = 0

    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count

my_list = [12, 7, 5, 64, 14, 33, 90]
even, odd = count_even_odd(my_list)

print("Even Numbers :", even)
print("Odd Numbers :", odd)

# Simple and easy to understand it
# Also we can take user input's also using input()


# Method 2 : (Using List Comprehension)

numbers = [10, 21, 4, 45, 66, 93, 1]
even_num = len([num for num in numbers if num % 2 == 0])
# Return length of numbers(num) for (num in numbers) only if num % 2 is equal to zero
odd_num = len([num for num in numbers if num % 2 != 0])
# Return length of numbers(num) num for (num in numbers) only if num % 2 is not equal to zero

print("Even Numbers :", even_num)
print("Odd Numbers :", odd_num)


# Method 3 : (Using filter() and lambda)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
# filter(function, iterable) : Use to filters the items in the list based on a condition.
# lambda x: x % 2 == 0 → this is a mini function that returns True for even numbers
# So, filter(lambda x: x % 2 == 0, numbers) means that : 
# Go through every number in the list, keep only the ones where x % 2 == 0 (i.e., even numbers)
# Same for that of filter(lambda x: x % 2 != 0, numbers)

print("Even Numbers :", len(even_numbers))
print("Odd Numbers :", len(odd_numbers))


# Method 4 : ()

even_count = sum(map(lambda x: x % 2 == 0, numbers))
odd_count = sum(map(lambda x: x % 2 != 0, numbers))
# map(function, iterable) applies the function to each item in the list
# lambda x: x % 2 == 0 returns True (which is 1) for even numbers, and False (which is 0) for odd numbers
# and the outer sum() will add all the values

print("Count of even number : ",even_count)
print("Count of odd number : ",odd_count)


# Method 5 : (Using while)

numbers = [10, 21, 4, 45, 66, 93, 1]
even_count = 0
odd_count = 0
i = 0

while i < len(numbers):
    if numbers[i] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    i += 1

print("Even Numbers:", even_count)
print("Odd Numbers:", odd_count)

# Method 1 : (Simple Loop with no function)

for num in range(10, 50):
    if num > 1 and all(num % i != 0 for i in range(2, num)):
        print(num, end=" ")
# Here The all() function checks if all values in an iterable (like a list, tuple etc) are True or not
print()

# Method 2 : (Simple Loops with function)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Here we use is_prime() to check the number is even or not from the range

def primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            # Here we call is_prime() if it return true then only the next condtion will work on
            primes.append(num)
            # If number is prime add it to primes[] list
    return primes

# Here we use primes_in_range() to get the range from the user 

print(primes_in_range(10, 50))
print()


# Method 3 : ( Using all() for Simplicity )

def is_prime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, n))
# Here we use shorthand for loop
# Here The all() function checks if all values in an iterable (like a list, tuple etc) are True or not

def primes_in_range(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]

print(primes_in_range(10, 50))
print()

# Method 4 : (Using List Comprehension)

print([n for n in range(10, 50) if all(n % i != 0 for i in range(2, n)) and n > 1])

numbers = [10, 21, 4, 45, 66, 93, 1]

even_count = [num for num in numbers if num % 2 == 0]

odd_count = [num for num in numbers if num % 2 != 0]

print("Even Numbers:", even_count)
print("Odd Numbers:", odd_count)
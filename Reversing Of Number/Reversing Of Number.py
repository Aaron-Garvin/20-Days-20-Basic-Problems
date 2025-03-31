print(' Program to Reverse a Number : ')
print('-----------------Method 1 : By Slicing-----------------')
print()
number=int(input(" Enter your number to be Reversed : "))

# Here we use int() function because the default type of input() function is string to covert string into integer we use int()
# The process of converting a data type into another data type is called as type casting

print("Your reversed number is : ", int(str(number)[::-1]))

# Here we convert the int to str again as slicing not work on int
# Slicing is the method by we can access a particular range of element
# So in, [::-1] repersents the step value as due to double colan(::)
# As the step value is negative it will print from the last to first pattern
# In last, we convert the str into int as we want number as a int

print()
print('-----------------Method 2 : While loop (Mathematical Approach)-----------------')
print()
num=int(input(" Enter your number to be Reversed : "))
rev = 0
while num > 0:
    rev = rev * 10 + num % 10      # Extract last digit and add to reversed number
    num //= 10                     # Remove last digit
print("Your reversed num is : ", rev)
print()



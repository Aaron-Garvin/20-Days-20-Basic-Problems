# Python program to find the max and min element in a list

# Method 1 : (BY Pre defined function)

Given_list_1 = [4, 7, 1, 9, 12, 3]

max_elem = max(Given_list_1)
min_elem = min(Given_list_1)

# Here max and min are the pre-defined function to know the max and min value

print("Maximum element is : ", max_elem)
print("Minimum element is : ", min_elem)
print()

# Method 2 : (Using sort)

Given_list_2 = [1,5,7,3,2,9,8,5,6,4]
Given_list_2.sort()

# Here sort() is a pre-defined function which sort the list in ascending order

min_value = Given_list_2[0]
max_value = Given_list_2[-1]

# Here we use negative index [-1] as the max will be in last index -1 represents the last index

print("Maximum value is : ", max_value)
print("Minimum value is : ", min_value)
print()

# Method 3 : (using loops)

Given_list_3 = [4,3,7,9,12,34,2,5,7,1]

max_num = Given_list_3[0]
min_num = Given_list_3[0]

# Here we assign the 0th index value to max and min both to compare with the rest 
 
for num in Given_list_3:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

# after comparison we get the values of max and min

print("Maximum number is : ", max_num)
print("Minimum number is : ", min_num)



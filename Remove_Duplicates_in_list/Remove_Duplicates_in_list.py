# Method 1 : (Using loop)

my_list = [1, 2, 2, 3, 4, 4, 5] # List containg duplicates
unique_list = [] # List for unique elements
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)

# This for loop iterate item over my_list
# And if block check if the item is present in the unique_list
# If item not in unique_list then add it into unique_list 
# append() : add element in the last

print(unique_list)


# Method 2 : (Using set() data type)

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(my_list))

# set() : It is a data type in Python that stores only unique elements
# and reconvert it into list
# this process is known as Type conversion

print(unique_list)


# Method 3 : (Using dict.fromkeys())

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(dict.fromkeys(my_list))

# As dict (Dictionary data type) can’t have duplicate keys
# Here dict.fromkeys(my_list) creates a dictionary where each item in the list becomes a key
# Then we convert the dictionary’s keys back into a list

print(unique_list)

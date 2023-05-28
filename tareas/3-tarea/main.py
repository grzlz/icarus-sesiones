# 1. Write a function that creates a list of 5 elements

def first_function():
    return [1, 2, 3, 4, 5]

# 2. Write a function that accesses and prints the third item from the list
def second_function(my_list):
    return my_list[2]

# 3. Write a function than prints the length of a list
def third_function(my_list):
    return len(my_list)

# 4. Write a program that modifies the second item in a list to be "Ola k ase"
def fourth_function(my_list):
    my_list[1] = "Ola k ase"
    return my_list

# 5. Write a function that adds a new item to the end of a list
def fifth_function(my_list, item):
    my_list.append(item)
    return my_list

# 6. Write a function that prints the second half o a list
def sixth_function(my_list):
    middle_index = len(my_list)//2
    print(my_list[middle_index:])

sixth_function([1,2,4, 6])
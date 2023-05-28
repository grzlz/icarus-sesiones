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

# 7. Write a function that creates a nested list and prints out the second element in the second list
def seventh_function():
    nested_list = [[6, 7, 8, first_function()]]
    print(nested_list[0][1])

# 8. Write a function that iterates over a list using a for loop and prints each element
def eight_function(my_list):
    for item in my_list:
        print(item)

# 9. Write a function that creates a list of squares por numbers 1 - 10
def ninth_funtion():
    my_list = range(1,11)
    squared_list = [i ** 2 for i in my_list]

    return squared_list

# 10. Write a function that takes two lists of numbers and returns a new list which is the result of multiplying each element of the first list by its corresponding element in the second list
def tenth_function():
    list1 = range(10)
    list2 = range(1,11)
    new_list = [i * j for i,j in zip(list1, list2)]

    return new_list

# 11. Write a function that calculates and prints the sum of all numbers in a list
def eleven(my_list):
    total = 0
    for i in my_list:
        total += i
    print(total)

# 12. Write a funciton that calculates and prints the multiplication of all numbers in a list
def twelve(my_list):
    total = 1
    for i in my_list:
        total *= i
    print(total)

# 13. Write a function that prints the maximum and minimum value of a list
def thirteen(my_list):
    print(f"Max: {max(my_list)}, min: {min(my_list)}.")

# 14. Write a function that removes duplicates from a list
def fourteen(my_list):
    new_list = []
    for item in my_list:
        if item not in new_list:
            new_list.append(item)
    return new_list


# 15. Write a function that reverts the order of a list

def fifteen(my_list):
    return my_list[::-1]
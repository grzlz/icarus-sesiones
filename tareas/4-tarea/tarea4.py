# 1. Create a dictionary where keys are integers from 1 to 5, and values are the square of the keys.
def square_keys():
    my_dict = {i: i**2 for i in range(1,6)}

    return my_dict

# 2. Given a dictionary, access and print a specific key's value.
def print_dict_key(input_dict, key):
    print(input_dict.get(key))

# 3. Write a function that takes a dictionary and a key-value pair, then adds the key-value pair to the dictionary if the key doesn't already exist.
def add_to_dict(input_dict, key, value):
    input_dict2 = input_dict.copy()
    if key in input_dict2:
        print("We already have a value for that")
    else:
        input_dict2[key] = value

    return input_dict2

# 4. Write a function that deletes a key-value pair from a dictionary, given a specific key.
def remove_from_dict(input_dict, key):
    if key in input_dict:
        del input_dict[key]
    else:
        print("No such key.")

    return input_dict

# 5. Write a program to check if a key exists in a dictionary.
def verify_key(input_dict, key):
    if key in input_dict:
        print("We got the key!")
    else:
        print("No key here")

# 6. Write a function that iterates over a dictionary and prints all key-value pairs.
def print_items(input_dict):
    for key, value in input_dict.items():
        print(key, value)

# 7. Use dictionary comprehension to create a dictionary that maps numbers from 1 to 10 to their squares.
def dict_comp():
    my_dict = {i: i**2 for i in range(1, 11)}
    
    return(my_dict)

# 8. Write a function that takes two lists of equal length as input and returns a dictionary where the elements of the first list are keys, and elements of the second list are values.
def lists_to_dict(list1, list2):
    if len(list1) == len(list2):
        return {i: j for i, j in zip(list1, list2)}
    else:
        raise ValueError("Lists must be of equal length")

# 9. Write a function that finds and returns the key with the maximum value in a dictionary.
def max_value(input_dict):
    key = [key for key in input_dict if input_dict[key] == max(input_dict.values())]
    return key[0]


# 10. Write a function that takes a dictionary as input and returns a list of all the values in the dictionary.
def dict_list(input_dict):
    return [i for i in input_dict.values()]

# 11. Write a program that sorts and prints a dictionary by its keys.

# 12. Write a program that sorts and prints a dictionary by its values.

# 13. Given a list of words, write a function that returns a dictionary where keys are words and values are the count of each word in the list.



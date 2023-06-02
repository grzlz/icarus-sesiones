# 1. Create a dictionary where keys are integers from 1 to 5, and values are the square of the keys.
def square_keys():
    my_dict = {i: i**2 for i in range(1,6)}
    return my_dict

# 2. Given a dictionary, access and print a specific key's value.
def print_dict_key(input_dict, key):
    print(input_dict.get(key))

print_dict_key(square_keys(), 2)

# 3. Write a function that takes a dictionary and a key-value pair, then adds the key-value pair to the dictionary if the key doesn't already exist.

# 4. Write a function that deletes a key-value pair from a dictionary, given a specific key.

# 5. Write a program to check if a key exists in a dictionary.

# 6. Write a function that iterates over a dictionary and prints all key-value pairs.

# 7. Write a program to calculate and print the number of key-value pairs in a dictionary.

# 8. Use dictionary comprehension to create a dictionary that maps numbers from 1 to 10 to their squares.

# 9. Write a function that takes two lists of equal length as input and returns a dictionary where the elements of the first list are keys, and elements of the second list are values.

# 10. Write a function that takes a dictionary as input and returns a list of all the values in the dictionary.

# 11. Write a program that sorts and prints a dictionary by its keys.

# 12. Write a program that sorts and prints a dictionary by its values.

# 13. Given a list of words, write a function that returns a dictionary where keys are words and values are the count of each word in the list.

# 14. Write a function that merges two dictionaries and returns the result.

# 15. Write a function that finds and returns the key with the maximum value in a dictionary.

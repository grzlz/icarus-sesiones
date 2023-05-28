def get_sum(my_list):
    my_sum = 0

    for number in my_list:
        my_sum += number

    return my_sum

def sum_to_item(my_list):

    new_list = []

    for number in my_list:
        new_list.append(number + 1)

    return new_list


example = [1, 2, 3]

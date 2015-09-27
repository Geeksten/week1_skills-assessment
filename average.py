def average(number_list):
    """Return the average (mean) of the list of numbers given.

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty. It's fine if
    this raises an error when given an empty list.
    """
    list_sum = 0
    for num in number_list:
        list_sum += num
    average_nums = (float(list_sum)/(len(number_list)))
    return average_nums

print average([2, 12, 3])
print average([])

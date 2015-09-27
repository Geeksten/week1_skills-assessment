def sum_numbers(number_list):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does this -- but for
    this exercise, you should not use it.

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero:

        >>> sum_numbers([])
        0

    """
#list = [1,2,3,4,5]

    list_sum = 0
    for num in number_list:
        list_sum += num
    return list_sum

print sum_numbers([1, 2, 3, 10])
print sum_numbers([])

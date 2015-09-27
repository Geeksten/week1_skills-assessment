def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []

    """
    for num in number_list[:]:
        if num % 2 == 0:
            number_list.remove(num)
    return number_list

print all_odd([1, 2, 7, -5])
print all_odd([2, -6, 8])

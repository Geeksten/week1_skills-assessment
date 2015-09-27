def all_even(number_list):
    """Return a list of only the even numbers in the input list.

        >>> all_even([2, 6, -1, -2])
        [2, 6, -2]

        >>> all_even([-1, 3, 5])
        []

    """
    for num in number_list[:]:
        if num % 2 != 0:
            number_list.remove(num)
    return number_list
    #return ['the wrong thing']

print (all_even([2, 6, -1, -2]))
print (all_even([-1, 3, 5]))
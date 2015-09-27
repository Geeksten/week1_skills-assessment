def smallest_int(number_list):
    """Find the smallest integer in a list of integers and return it.

        >>> smallest_int([-5, 2, -5, 7])
        -5

    If the input list is empty, return None:

        >>> smallest_int([]) is None
        True

    """
    for num in number_list[:]:
        return min(number_list)

        # find minimum value

print smallest_int([-5, 2, -5, 7])
print (smallest_int([]) is None)


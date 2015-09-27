def largest_int(number_list):
    """Find the largest integer in a list of integers and return it.

        >>> largest_int([-5, 2, -5, 7])
        7

    If the input list is empty, return None:

        >>> largest_int([]) is None
        True

    """
    for num in number_list[:]:
        return max(number_list)
    #return 0
print largest_int([-5, 2, -5, 7])
print (largest_int([]) is None)

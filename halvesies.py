def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are, make sure you don't round off the half:

        >>> halvesies([1, 5])
        [0.5, 2.5]

    """
    index = 0
    #empty list to hold the halves. we will append to this as we go
    list_of_halves = []
    while number_list[index] < len(number_list):
        for num in number_list:
            half = (float(num)/2)
            list_of_halves.append(half)

        index = index + 1
    return list_of_halves

print halvesies([2, 6, -2])
print halvesies([1, 5])

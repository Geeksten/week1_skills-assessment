def mult_numbers(number_list):
    """Return product (result of multiplication) of the numbers in the list.

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in the input, the product will be zero:

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product, if the list is
    empty, the product should be 1:

        >>> mult_numbers([])
        1

    """
    list_mult = 1
    for num in number_list:
        list_mult *= num
    return list_mult

print mult_numbers([1, 2, 3])
print mult_numbers([10, 20, 0, 50])
print mult_numbers([])   
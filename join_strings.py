def join_strings(word_list):
    """Return a string of all input strings joined together.

    Python ha a built-in method on lists, `join` -- but this exercise, you
    should not use it.

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string:

        >>> join_strings([])
        ''

    """
    result_string = ''
    for element in word_list:
        result_string += element
    return result_string
print join_strings(["spam", "spam", "bacon", "balloonicorn"])
print join_strings([])
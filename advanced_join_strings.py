

# Uncomment the function below to work on the advanced problem.
# Tip: To comment or uncomment blocks of code, highlight what you want to
#    comment or uncomment, and then CMD+"/" or CTRL-"/"

def advanced_join_strings(list_of_words):
    """Return a single string with each word from the input list
    separated by a comma.

        >>> advanced_join_strings(["Labrador", "Poodle", "French Bulldog"])
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course:

        >>> advanced_join_strings(["Pretzel"])
        'Pretzel'

    """

#    result_string = ''
    return ','.join(list_of_words)
    #    result_string += element
    #return result_string

print advanced_join_strings(["Labrador", "Poodle", "French Bulldog"])
print advanced_join_strings(["Pretzel"])

# END OF ASSIGNMENT: You can ignore everything below

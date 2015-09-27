def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """
    list_of_longs = []
    for word in word_list:
        if len(word) < 5:
            continue
        list_of_longs.append(word)
    return list_of_longs

print (long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"]))
print (long_words(["all", "are", "tiny"]))
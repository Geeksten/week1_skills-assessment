def word_lengths(word_list):
    """Return the length of words in the input list.

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]

    """
    length_of_words_list = []
    #while word_list[index] < len(word_list):
    for word in word_list[:]:
        the_word_length = len(word)
        length_of_words_list.append(the_word_length)

    #index = index + 1
    return length_of_words_list
    #return []
print word_lengths(["hello", "hey", "hello", "spam"])

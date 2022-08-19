def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_phrase_list = []
    phrase_list = [ltr for ltr in phrase]
    for ltr in phrase_list:
        if ltr.upper() == to_swap.upper():
           new_phrase_list.append(ltr.swapcase())
        else:
            new_phrase_list.append(ltr)
    return "".join(new_phrase_list)

def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    # phrase_list =[word for word in phrase.upper()]
    # reversed_phrase_list = []
    # for idx in range(len(phrase)-1, -1, -1):
    #     reversed_phrase_list.append(phrase[idx].upper())
    # if phrase_list == reversed_phrase_list:
    #     return True
    # else:
    #     return False

    phrase_upper = phrase.upper().replace(' ', '')
    phrase_reversed = phrase_upper[::-1]
    return phrase_upper == phrase_reversed:
    #     return True
    # else:
    #     return False




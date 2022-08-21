def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    # reverse_string = []
    # phrase_length = len(phrase)
    # for idx in range(phrase_length-1, -1, -1):
    #     reverse_string.append(phrase[idx])
    # return "".join(reverse_string)
    
    return phrase[::-1]
    


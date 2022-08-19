def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    list_s = [char for char in s]
    position = []
    vowels = []
    for x in range(len(s)):
        if list_s[x] in 'aeiouAEIOU':
           position.append(x)
           vowels.append(list_s[x])

    vowels.reverse()

    for y in range(len(position)):
        list_s[position[y]] = vowels[y]
    
    return "".join(list_s)


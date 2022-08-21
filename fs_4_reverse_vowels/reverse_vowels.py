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
    # my solution stored the position of vowels and vowels itself 
    list_s = [char for char in s]
    position = []
    vowels = []
    for x in range(len(s)):
        if list_s[x] in 'aeiouAEIOU':
           position.append(x)
           vowels.append(list_s[x])
    # reversed stored vowels
    vowels.reverse()
    # put back the reversed vowels into the positions of previous vowels by using position list.
    for y in range(len(position)):
        list_s[position[y]] = vowels[y]
    
    return "".join(list_s)

    # springboard answer
    # they just used .lower() to compare both upper and lowercase at the same time.
    # they checked the letter from the start and the end at the same time and if there is a vowel swap it
    # and at the end joined the list into string.
    # make a set of aeiou
    vowels = set('aeiou')
    # make string into a list
    string= list(s)
    head = 0
    tail = len(s)-1 

    while head > tail:
        if string[head].lower not in vowels:
            # added +1 to move on to next letter
            head +=1
        elif string[tail].lower not in vowels:
            # minus 1 from tail to move down to next letter from the end
            tail -=1
        # if both of letters are in vowels switch them and advance letters 
        else:
            string[head], string[tail] = string[tail], string[head]
            head += 1
            tail -+1
    
    return "".join()




def truncate(phrase, n):
    """Return truncated-at-n-chars version of  phrase.
    
    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """
    
    # make string into list
    phrase_list =[char for char in phrase]

    # check if n is less than 3
    if n < 3:
        return 'Truncation must be at least 3 characters.'
    # check if length of list is smaller than n
    if len(phrase_list) < n:
        return ''.join(phrase_list)
    # check if length of list is the same or longer than n
    if len(phrase_list) >= n:
        phrase_list[n-3:] = ['...']
        return ''.join(phrase_list)
        

   
def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
    # boolean = []
    # for idx in range(0, len(a)-1):
    #     boolean.append(a[2][idx] in b[2])
    
    # if True in boolean:
    #     return True
    # else:
    #     return False

    if set(a[2] & set(b[2])): 
    # getting intersection of sets, if intersection exists
        return True
    else:
        return False

    # or 
       # return bool(set(a[2] & set(b[2])



            
        

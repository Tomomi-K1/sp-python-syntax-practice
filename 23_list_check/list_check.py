def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    # test = False
    for item in lst:
        if not isinstance(item, list):
            return False
    
    return True
        #     test = True
        # else:
        #     test = False
        
    # return test

def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """

    # springbaord answer
    out = {}

    for idx, val in enumerate(keys):
        out[val] = values[idx] if idx <len(values) else None

    return out

    # check if length of value is shoter than length of keys
    # new_dict = {}
    # if len(values) < len(keys):
    #     for idx in range(len(keys)):
    #         if idx > len(values)-1:
    #             new_dict[keys[idx]] = None
    #         else:
    #             new_dict[keys[idx]] = values[idx]
    #     return new_dict

    # # check if length of keys is shoter than length of value
    # if len(values) > len(keys):
    #     for idx in range(len(values)):
    #         if idx > len(keys)-1:
    #             break
    #         else:
    #             new_dict[keys[idx]] = values[idx]
    #     return new_dict
    # # if none of above, make list of keys into key of dict and list of values into values
    # else:
    #     new_dict = dict(zip(keys, values))
    #     return new_dict

 

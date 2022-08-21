def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """
    # fullname_list = []
    # for name in people:
    #     first_name =name.get('first')
    #     last_name =name.get('last')
    #     fullname_list.append(f'{first_name} {last_name}')
    # return fullname_list

    return [f'{person['first']} {person['last']}' for person in people]
        
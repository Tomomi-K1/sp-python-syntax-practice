def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    phrase = phrase.lower()
    return {char: phrase.count(char) for char in phrase if char in 'aeiou'}
    # for char in phrase:
    #     if char in 'aeiou':
    #         return {char: phrase.count(char)}

    # springboard answer

    # phrase = phrase. lower()
    # counter = {}

    # for ltr in phrase:
    #     counter[ltr] = counter.get(ltr, 0) + 1

# get() Parameters
# get() method takes maximum of two parameters:

    # key - key to be searched in the dictionary ==> here 'ltr' is the key
    # value (optional) - Value to be returned if the key is not found. The default value is None. ==> here 0 is the value returned if the key is not found
    # if counter[ltr] is being created for the first time the get will return value 0 then plus 1. if key already created then 
    # it will .get method will pull the value from the key and then add 1 

def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    opening ='('
    closing =')'
    stack = []
    # if string length is odd, then not valid parens
    if len(parens) % 2 != 0:
        return False
    # iterate through the string and check following
    for x in parens:
        # check if first one is opening parens
        if x == opening:
            stack.append(x)
        elif x == closing:
            if stack == []:
                return False
                break
            elif stack[-1] == opening:
                stack.pop()
            else:    
                return False
                break
    if stack != []:
        return False
    else:
        return True
            
        
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
    # opening ='('
    # closing =')'
    # stack = []
    # # if string length is odd, then not valid parens
    # if len(parens) % 2 != 0:
    #     return False
    # # iterate through the string and check following
    # for x in parens:
    #     # check if first one is opening parens
    #     if x == opening:
    #         stack.append(x)
    #     elif x == closing:
    #         if stack == []:
    #             return False
    #             break
    #         elif stack[-1] == opening:
    #             stack.pop()
    #         else:    
    #             return False
    #             break
    # if stack != []:
    #     return False
    # else:
    #     return True

    # springboard answer
    count = 0
    # loop through each parenthese and if opening paren, add 1 and closing, -1 so at the end the count should be 0.
    for p in parens:
        if p == '(':
            count += 1
        elif p == ')':
            count -=1

        # if ')' comes first, count will be -1, then it will return False and end the loop
        if count<0:
            return False
    # if count is not 0, it means not valid so it will return False.
    return count == 0            
        
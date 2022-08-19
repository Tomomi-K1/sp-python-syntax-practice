def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
            


    pair = ();
    for inc in range(1, len(nums)-1):
        for i in range(len(nums)-2):
            if i+inc > len(nums)-1:
                break
            if nums[i] + nums[i+inc] == goal:
                pair = (nums[i], nums[i+inc])
                return pair
    if len(pair) == 0:
        return pair

    # (num[0], num[1])//idx +1
    #  (num[1], num[2])
    #  (num[2], num[3])
    #  (num[0], num[2])//idx + 2
    #  (num[1], num[3])
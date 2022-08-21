def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """
    # springboard answer
    #  no need to specify when start was 0 or not 0 since default value is set to 0 
    # however when end is set to None we need to specify what the end would be
    if end is None:
        end = len(nums)
    
    return sum(nums[start:end+1])


    # # when start and end is given each value
    # if start != 0 and end != None:
    #     # if end is larger or the same number as nums length, sum to the end of list
    #     if end >= len(nums):
    #         new_nums = nums[start:]
    #     # if end is less than the length of nums list, sums from the start to end
    #     else:
    #         new_nums = nums[start:end+1]
    #     return sum(new_nums)
    # # when start has a value and end is set to None, sums from start to the end
    # if start != 0 and end == None:
    #     new_nums = nums[start:]
    #     return sum(new_nums)
    
    # # when start is 0 and end has a value,  
    # if start == 0 and end != None:
    #     new_nums = nums[:end+1]
    #     return sum(new_nums)

    # else:
    #     return sum(nums)


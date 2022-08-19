def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    num_dict = {num: nums.count(num) for num in nums}
    return max(num_dict, key=num_dict.get)
    # "key=" parametor will is the function that you want to run for each element before you run max method.
    # max will find the max value in dict and runs num_dict.get(num) => returns key information
            

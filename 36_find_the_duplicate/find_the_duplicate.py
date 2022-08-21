def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
    # springboard answer

    # Seenをセットで作る理由は、numをseenについかしたときにDuplicateがあるのを防ぐため
    seen = set()
    # numsをiterateして、もしnumがセットの中にあったらDuplicateがあったことになるので、それを返す。
    # Dupeがない場合は return numが走らないので、その場合このfunctionはexplicitにreturnを返してないので、Noneが返るので、わざわざreturn Noneはいらない
    for num in nums:
        if num in seen:
            return num
        seen.add(num)


    # new_dict ={num:nums.count(num) for num in nums}
    # if 2 in list(new_dict.values()):
    #     for key, value in new_dict.items():
    #         if value == 2 :
    #             return key
    # else:
    #     return None
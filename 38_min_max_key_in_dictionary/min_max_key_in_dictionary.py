def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
#    springboard asnwer
    # .keys() method returns LIST of keys... so I don't need to make it into a list by doing keys = list(d.keys())
     keys = d.keys() 

    # minとMaxはリストの中の最大値、最小値をみつけてくれる。もしリストが文字で形成されていたら、アルファベット順で最小、最大が決まる。
    # アルファベット最小はa 後に行くにつれて最大と考えられる　ｚが最大
     return (min(keys), max(keys))
    

    # keys = list(d.keys())
    # keys.sort()
    # return (keys[0], keys[-1])

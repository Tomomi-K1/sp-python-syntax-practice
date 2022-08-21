def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    weekday_list =['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if day_of_week >0 and day_of_week <=7:
        return weekday_list[day_of_week-1]
    # else: 
    #     return None
    
    #If we get to the end of any function and we have not explicitly executed any return statement, Python automatically returns the value "None". 
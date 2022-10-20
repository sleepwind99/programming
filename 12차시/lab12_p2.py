def moderateDays(mydict):
    '''Returns a list [...] of the days for which the average
    temperature was between 70 and 79 degrees.
    '''
    user_list = []
    for day in mydict.keys():
        if 70 <= mydict[day] and mydict[day] <= 79:
            user_list.append(day)

    return user_list
            
            

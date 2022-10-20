def countAllLetters(line):
    """ Counts letters in 'line' and returns result list. If the line does
        not contain any letter, returns an empty list."""
    #Make user list
    user_list = ['1']
    #Switch the received string to lowercase
    sline = line.lower()
    #Count and save the number of strings in the list.
    for i in sline:
        user_tell = True
        if i.isalpha():
        
            for e in range(0,len(user_list)):
                if user_list[e][0] == i:
                    user_list[e][1] += 1
                    user_tell =False
                
                        

            if user_tell == True:
                slist=[]
                slist.append(i)
                slist.append(1)
                user_list.append(slist)
    result = []
    del user_list[0]
    #Save the list in tuple format.
    for ch in range(0,len(user_list)):
        ud = (user_list[ch][0],user_list[ch][1])
        result.append(ud)
    #Sort and return the list.
    result.sort()
    return result
            

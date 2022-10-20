
user_tell = True

result = 0

#using while function
while user_tell == True :
    user_num = int(input('Your number: '))
    
    #Calculate for a given condition
    if user_num>0 and user_num<=100 :
        result = result + user_num

    #output result        
    elif user_num == 0 :
        user_tell = False
        print('Sum:',result)
       
    

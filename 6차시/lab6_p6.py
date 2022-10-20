#Make a loop for a given condition
while True :
    user_limit = int(input('Enter the limit L: '))
    first_num = user_limit
    #Loop is stop when user_limit is zero
    if user_limit == 0: break
    result = 0
    #Calculate the Sigma
    while user_limit > 0:
        result = result + (1/user_limit)
        user_limit = user_limit -1
    #Output result
    print('Sum of the initial',first_num,'term(s):',format(result,'.6f'))    

        

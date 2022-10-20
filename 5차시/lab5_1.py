
user_num_list = []
#Get user_num
user_num = float(input('Enter a number: '))
#Add number to list for condition
if user_num > 0 :
    user_num_list.append(user_num)
               
    while user_num > 0:
        user_num = float(input('Enter a number: '))
        user_num_list.append(user_num)
     #Store the largest value in the list as a result                  
    result = max(user_num_list)
    #Output result
    print('The largest number entered was',format(result,'.2f'))
                       
else:
    print('No positive number was entered')

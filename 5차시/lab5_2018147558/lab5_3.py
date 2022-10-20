#Create a while loop for a given condition 
user_tell = True
user_num_list = []
while user_tell == True:
    #Get user integer
    user_num = int(input('Enter an integer: '))
    #When user integer over the 100 save user_num 'over'
    if user_num > 100:
        user_num = 'over'
        user_num_list.append(user_num)
    #When user integer  equal the 0 output result
    elif user_num == 0:
        print(user_num_list)
        user_tell = False
    #Else value save user_num_list
    else :
        user_num_list.append(user_num)

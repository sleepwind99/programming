#Get user name
user_name = input('Enter a first and last name: ')
first_name = ''
last_name = ''
user_tell = True
#filtering  gap to criteria
for name_list in user_name:
    if name_list == ' ':
        if first_name != '':
            user_tell = False
            
    elif user_tell == True:
        first_name += name_list
    else :
        last_name += name_list
#Output result
print(last_name +', '+ first_name[0] +'.') 
    

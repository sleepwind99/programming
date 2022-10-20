#Get user name
user_name = str(input('Enter a name (q to quit): '))
#Create condition to use while loop
user_tell = True
result = user_name.count('a')+user_name.count('A')
while user_tell == True:
    if user_name =='q' :
        #Output result when user_name is 'q'
        print("Appearance of letter 'a':",result)
        user_tell = False

    else :
        user_name = str(input('Enter a name (q to quit): '))
        result = result + user_name.count('a') + user_name.count('A')
   

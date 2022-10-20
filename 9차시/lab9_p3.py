import math
#Get string to user
user_str = input('Enter string to check: ')
#Divide user string to half
str_first = user_str[0:len(user_str)//2]
last_range = math.ceil(len(user_str)/2)
str_second = ''
#Make sure that the user string, divided in half, is the same.
for i in range(len(user_str),last_range,-1):
    str_second += user_str[i-1]
#Output result
if str_first == str_second:
    print(user_str,'is a palindrome')
else:
    print(user_str,'is NOT a palindrome')
    
    
    

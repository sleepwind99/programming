#Get user EAN
user_EAN = int(input('Enter the first 12 digits of an EAN: '))

#Extract 12 numbers
user_EAN_1 = user_EAN%10**12//10**11
user_EAN_2 = user_EAN%10**11//10**10
user_EAN_3 = user_EAN%10**10//10**9
user_EAN_4 = user_EAN%10**9//10**8
user_EAN_5 = user_EAN%10**8//10**7
user_EAN_6 = user_EAN%10**7//10**6
user_EAN_7 = user_EAN%10**6//10**5
user_EAN_8 = user_EAN%10**5//10**4
user_EAN_9 = user_EAN%10**4//10**3
user_EAN_10 = user_EAN%10**3//10**2
user_EAN_11 = user_EAN%10**2//10
user_EAN_12 = user_EAN%10

#Calculate first and second sum
user_EAN_first_sum = user_EAN_2+user_EAN_4+user_EAN_6+\
                     user_EAN_8+user_EAN_10+user_EAN_12
user_EAN_second_sum = user_EAN_1+user_EAN_3+user_EAN_5+\
                      user_EAN_7+user_EAN_9+user_EAN_11

#Calculate result
user_EAN_result = 9-((((user_EAN_first_sum*3)+user_EAN_second_sum)-1)%10)
#output result
print('Check digit:',user_EAN_result)

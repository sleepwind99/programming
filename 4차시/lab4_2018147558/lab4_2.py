#Declare a variable
num = 1

#Use the while function in a given condition
while num<=100 :

    #Indend when the result is a multiple of 10
    if num%10 == 0 :
        print(format(num, '>3'))
        num = num + 1

    #Paste when the result is not a multiple of 10
    else :
        print(format(num, '>3'), end='')
        num = num + 1

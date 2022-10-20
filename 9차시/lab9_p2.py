import stack
#Make loop that stops at a given condition
while True:
    #Get RPN expression to user
    user_RPN = input('Enter an RPN expression: ')
    #If the calculation is made according to the given conditions or
    #incorrect conditions are found, an error statement is printed
    if user_RPN == 'q': break
    
    else:
        user_list = stack.getStack()
        if user_RPN[len(user_RPN)-1] != '=':
            print('Evaluation error')
        else:
            user_tell=True
            for num in user_RPN:
                if num == '+':
                    if len(user_list) >= 2:
                        a = int(stack.top(user_list))
                        stack.pop(user_list)
                        b = int(stack.top(user_list))
                        stack.pop(user_list)
                        stack.push(user_list,a+b)
                    else:
                        print('Evaluation error')
                        user_tell = False
                        

                elif num == '-':
                    if len(user_list) >= 2:
                        a = int(stack.top(user_list))
                        stack.pop(user_list)
                        b = int(stack.top(user_list))
                        stack.pop(user_list)
                        stack.push(user_list,b-a)
                    else:
                        print('Evaluation error')
                        user_tell = False

                elif num == '*':
                    if len(user_list) >= 2:
                        a = int(stack.top(user_list))
                        stack.pop(user_list)
                        b = int(stack.top(user_list))
                        stack.pop(user_list)
                        stack.push(user_list,a*b)
                    else:
                        print('Evaluation error')
                        user_tell = False


                elif num == '/':
                    if len(user_list) >= 2:
                        a = int(stack.top(user_list))
                        stack.pop(user_list)
                        b = int(stack.top(user_list))
                        stack.pop(user_list)
                        stack.push(user_list,b/a)
                    else:
                        print('Evaluation error')
                        user_tell = False


                elif num == '=' and user_tell == True:
                    if len(user_list) != 1:
                        print('Evaluation error')
                    else :
                        result = float(user_list[0])
                        if float.is_integer(result) == True:
                            print('Value of expression:',int(result))
                        else :
                            print('Value of expression:',format(result,'.2f'))


                else:
                    stack.push(user_list,num)
            

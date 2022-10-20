import stack
#Get user input
user_input = input('Enter parentheses and/or braces: ')
#Make new stack
user_stack = stack.getStack()
user_tell = True
#Distinguish user input to given condition
for i in user_input:
    
    if i == '(':
        stack.push(user_stack,'(')
        
    elif i == '{':
        stack.push(user_stack,'{')
        
    elif i == ')':
        if stack.top(user_stack) != '(':
            user_tell = False
        stack.pop(user_stack)
        
    elif i == '}':
        if stack.top(user_stack) != '{':
            user_tell = False
        stack.pop(user_stack)
#Output result       
if user_tell == True:
    print('Nested properly.')
else:
    print('Not properly nested.')
        

#Get user number
user_num = int(input('Enter a number: '))

mulp = 1
result = 1
#Using while function and Caculate result
while user_num// mulp> 10 :
    mulp = mulp*10
    result = result+1
#Using if function and output result    
if result == 1 :
    print('The number',user_num,'contains',result,'digit')

else :
    print('The number',user_num,'contains',result,'digits')

#Get user integer
user_num = int(input('Enter an integer: '))
gap_size = user_num*2-1               
#Use the while function to place *                
while user_num >= 1:
    point_num = user_num*2-1           
    gap = (gap_size-point_num)//2       
    print(' '*gap,end='')
    print('*'*point_num)
    user_num = user_num-1

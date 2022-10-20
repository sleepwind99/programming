#Get user fraction
user_calculate = input('Enter a fraction: ')
first_num_list = []
last_num_list = []
first_num = ''
last_num = ''
user_tell = False
#Distinguish the unmbers according to a given condition
for user_num in user_calculate:
    if user_num != '/' and user_num != ' ':
        if user_tell== False:
            first_num_list.append(user_num)
        else :
            last_num_list.append(user_num)
        
    elif user_num == '/':
        user_tell = True
        
for e in range(0,len(first_num_list)):
    first_num += first_num_list[e]
for i in range(0,len(last_num_list)):
    last_num += last_num_list[i]
first_num = int(first_num)
last_num = int(last_num)
#Calculate 
if first_num <= last_num :
    large = last_num
    small = first_num
else :
    large = first_num
    small = last_num

rest = large % small

while rest != 0 :
    large = small
    small = rest
    rest = large % small
#Output result
print('In lowest terms: ',first_num//small,'/',last_num//small,sep='')

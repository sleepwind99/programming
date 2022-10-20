#Get user's name
user_name_gap = input('Enter a first and last name: ')
#Delete both side gap
user_name = user_name_gap.strip()
#Indexing gap plase
gap_num = user_name.index(' ')
#define first_name and last_name
first_name = user_name[:gap_num]
last_name = user_name[gap_num+1:]
last_name.strip()
#output result
print(last_name+', '+first_name[0]+'.')
    

        
    

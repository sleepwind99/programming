#Get user_ISBN
user_ISBN = input('Enter an ISBN: ')
#Eliminate - in user_ISBN
ISBN = user_ISBN.split('-')
#Output result
print(format(ISBN[0],'.<20'),'GS1 prefix',sep='')
print(format(ISBN[1],'.<20'),'Group identifier',sep='')
print(format(ISBN[2],'.<20'),'Publisher code',sep='')
print(format(ISBN[3],'.<20'),'Item number',sep='')
print(format(ISBN[4],'.<20'),'Check digit',sep='')

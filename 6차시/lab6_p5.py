ufkg = ['q']
#Make a loop for given condition
while True :
    #Get fruit name
    uf = input('Enter a fruit type (q to quit): ')
    #If fruit name is 'q' then loop stop
    if uf == 'q':
        break
    else :
        user_tell = False
        #Get fruit weight
        kg = int(input('Enter the weight in kg: '))
        for e in range(0,len(ufkg)):
            if uf == ufkg[e][0] :
                ftkg = []
                ufkg[e][1] = ufkg[e][1] + kg
                user_tell = True
            
        if user_tell == False:
            ftkg =[]
            ftkg.append(uf)
            ftkg.append(kg)
            ufkg.append(ftkg)
        
#Sorting and output result            
del ufkg[0]
ufkg.sort()
for i in range(0,len(ufkg)):
    print(ufkg[i][0] +', '+ str(ufkg[i][1]) +'kg.')
                



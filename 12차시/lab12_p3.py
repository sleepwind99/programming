#Get user file name
user_file = input('Enter a filename: ')
import random
#Encrypt if user extension is txt
if user_file[-3:] == 'txt':
    enc_file = open(user_file[:-3]+'enc','w')
    key_file = open(user_file[:-3]+'key','w')
    org_file = open(user_file,'r')
    #Generate random key 
    key_list,key_list_chr = [],[]
    for e in range(97,123):
        key_list.append(e)
    for e in range(65,91):
        key_list.append(e)
    for e in range(48,58):
        key_list.append(e)
    key_list.append(32)
    for e in key_list:
        key_list_chr.append(chr(e))
        
    key_list_1 = random.sample(key_list_chr,63)
    key_list_2 = random.sample(key_list_chr,63)
    a,key = [],[]
    
    for e in range(0,63):
        a.append(key_list_1[e])
        a.append(key_list_2[e])
        key.append(a)
        a = []
    #Make key file
    for e in range(0,len(key)):
        key_file.write(key[e][0]+','+key[e][1]+'\n')
    #Encrypt orginal file
    for line in org_file:
        a = ''
        for e in line:
            c = False
            for i in range(0,len(key)):
                if e == key[i][0]:
                    a+= key[i][1]
                    c = True
            if c == False:
                a += e
        enc_file.write(a)
    #Close opened file
    enc_file.close()
    org_file.close()
    key_file.close()
#Decrypt if user extension is enc
elif user_file[-3:] == 'enc':
    con_file = open(user_file[:-3]+'key','r')
    con_line = con_file.readline()
    line_list = []
    #Make Decrypt key to list
    while con_line != '':
        line_list.append(con_line.strip('\n').split(','))
        con_line = con_file.readline()
    
    file_name = user_file[:-3]+'txt'
    txt_file = open(file_name,'w')
    enc_file = open(user_file,'r')
    #Decrypt enc file
    for line in enc_file:
        a = ''
        for e in line:
            c = False
            for i in range(0,len(line_list)):
                if e == line_list[i][1]:
                    a += line_list[i][0]
                    c = True
            if c == False:
                a += e
        txt_file.write(a)
    #Close opened file
    enc_file.close()
    txt_file.close()
    con_file.close()
                
        
            
    
        
            

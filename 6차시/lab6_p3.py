# Password Encryption/Decryption Program

# init
password_out = ''
case_changer = ord('a') - ord('A')
encryption_key = (('a','m'), ('b','h'), ('c','t'), ('d','f'), ('e','g'),
  ('f','k'), ('g','b'), ('h','p'), ('i','j'), ('j','w'), ('k','e'),('l','r'),
  ('m','q'), ('n','s'), ('o','l'), ('p','n'), ('q','i'), ('r','u'), ('s','o'),
  ('t','x'), ('u','z'), ('v','y'), ('w','v'), ('x','d'), ('y','c'), ('z','a'),
  ('#','!'), ('@','('), ('%',')'))

encrypting = True
user_tell = True
# get password
password_in = input('Enter password: ')

# perform encryption / decryption
if encrypting:
    from_index = 0
    to_index = 1
else:
    from_index = 1 
    to_index = 0
alpa = False
g = False
digit = False
case_changer = ord('a') - ord('A')

if len(password_in) > 1 :


    for ch in password_in:
    
    
        if ('a' <= ch and ch <= 'z')or('A' <= ch and ch <= 'Z'):
            alpa = True
        elif (ch=='#' or ch=='@' or ch=='%') :
            g = True
        elif ('0' <= ch and ch <='9') :
            digit = True
        else :
            user_tell = False
            break


    if (user_tell == True) and (alpa ==True) and (g==True) and (digit==True):            
        for ch in password_in:
            letter_found = False
    
            for t in encryption_key:
                if ('a' <= ch and ch <= 'z'or ch=='#' or ch=='@' or ch=='%') and ch == t[from_index]:  
                    password_out = password_out + t[to_index]
                    letter_found = True
                elif ('A' <= ch and ch <= 'Z') and chr(ord(ch) + 32) == t[from_index]:
                    password_out = password_out + chr(ord(t[to_index]) - case_changer)
                    letter_found = True
            if not letter_found:
                password_out = password_out + ch
            
# output
        if encrypting:
            print('Your encrypted password is:', password_out)
        else:
            print('Your decrypted password is:', password_out)     
    else :
        print('Invalid password!')
            
else :
    print('Invalid password!')
    



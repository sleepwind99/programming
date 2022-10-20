def copyFiles(f1,f2,f3):
    """ Copies f1 and f2 onto f3.
        The function assumes that files f1 and f2 can be opened, and that
        no error occurs in writing file f3.
        Therefore, the function will always return 0.
        (Error handling with file I/O will be part of next week's lecture.)"""
    #Open file f1 and f2 to read
    str1 = open(f1,'r')
    str2 = open(f2,'r')
    #Open file f3 to write
    str3 = open(f3,'w')
    #Read line in file f1 and copy to f3
    for line in str1:
        str3.write(line)
        
    str3.write('\n')
    #Read line in file f2 and copy to f3
    for line in str2:
        str3.write(line)
    #Close all file
    str1.close()
    str2.close()
    str3.close()
        
    


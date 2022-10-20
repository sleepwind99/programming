def copyFiles(f1,f2,f3):
    """ Copies f1 and f2 onto f3.
        If f1, f2 or f3 cannot be opened, -1 is returned.
        otherwise, the copy operation is performed and 0 is returned"""
    try:
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
        return 0

    except IOError:
        return -1
    #Close all file
    str1.close()
    str2.close()
    str3.close()
        
    


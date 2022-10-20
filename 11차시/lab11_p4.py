def getFile():
    '''
        Returns the file name and associated file object for reading the
        file  as tuple of the form (file_name, input_file).
    '''
    input_file_opened = False
    while not input_file_opened:
        try:
            file_name = input('Enter input file name (with extension): ')
            input_file = open(file_name, 'r')
            input_file_opened = True
        except IOError:
            print ('Input file not found - please reenter')
    return (file_name, input_file)

def countWords(file_name, input_file):
    ''' Returns the number of occurrences
        of search_word in the provided input_file object.'''
    word_list = ['\n']
    word_delimiters = [' ', ',', ';', ':', '.','\n',
                       '"',"'", '(', ')']
    file = file_name[0:len(file_name)-3]+'wc'
    copy_file = open(file,'w')
    for line in input_file:
        copy_file.write(line)
        line = line.lower() # convert to lower case characters.
        word = ''
        #Sort and distinguish word
        for e in line:
            if e in word_delimiters:
                user_tell = True
                for i in range(0,len(word_list)):
                    if word_list[i][0] == word:
                        word_list[i][1] += 1
                        user_tell = False
                    elif word == '':continue
                if user_tell == True:
                    case1 = [word,1]
                    word_list.append(case1)
                word = ''
            else:
                word += e
    del word_list[0]
    word_list.sort()
    for e in range(0,len(word_list)):
        print(word_list[e][0]+': '+str(word_list[e][1]))
    #Make copy file to .wc 
    file = file_name[0:len(file_name)-3]+'wc'
    copy_file = open(file,'w')
    for line in input_file:
        copy_file.write(line)
#------main
file_name, input_file = getFile()
countWords(file_name, input_file)





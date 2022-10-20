def countLetters(line):
    """Count all letter characters in string ``line'' and write the
        result to file ``answer.txt''.
        
        The number of letter characters must be written to the file:
        countLetters('abA1 23') -> writes 3
        countLetters('!') -> writes 0"""
    user_list = []
    for ch in line:
        if ch.isdigit():
            user_list.append(ch)
    #count user_list
    num = len(user_list)
    user_text = open("answer.txt",'w')
    user_text.write(str(num) + '\n')
    user_text.close()

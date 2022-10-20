#Get first user word
user_word = input('Enter a word (q to quit): ')
#Make user word list
user_word_list = []
if user_word != 'q':
    while user_word != 'q':
        user_tell = False
        user_word_first = user_word[0]
        #Assing a string to a condition
        for ch in range(1,len(user_word)) :
            if user_word[ch] == user_word_first.upper() or user_word[ch] == user_word_first.lower():
                user_tell = True
            else :continue
        if user_tell == True :
            user_word_list.append(user_word)
        user_word = input('Enter a word (q to quit): ')
    user_word_list.sort()
    print(user_word_list)
#When first user word is 'q', Output result
else : print(user_word_list)
 

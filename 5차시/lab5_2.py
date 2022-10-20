#Get sentence from user
user_sentence = str(input('''Enter a sentence: '''))

#Calcurate result value
result = user_sentence.count('a') + user_sentence.count('e')\
          + user_sentence.count('i') + user_sentence.count('u')\
          + user_sentence.count('o') + user_sentence.count('A')\
          + user_sentence.count('E') + user_sentence.count('I')\
          + user_sentence.count('O') + user_sentence.count('U')


#Output result
if result == 1:
    print('Your sentence contains',result,'vowel.')
else:
    print('Your sentence contains',result,'vowels.')

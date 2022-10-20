#Get user color code
user_color = input('Enter a color: ')
#Save hex as decimal in the dictionary
color_rule = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5\
              ,'6':6,'7':7,'8':8,'9':9\
              ,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
#Make all alphabet to lower-case
user_color = user_color.lower()
red = color_rule[user_color[0]]*16 + color_rule[user_color[1]]
green = color_rule[user_color[2]]*16 + color_rule[user_color[3]]
blue = color_rule[user_color[4]]*16 + color_rule[user_color[5]]
#Output result
print('Red:',red)
print('Green:',green)
print('Blue:',blue)

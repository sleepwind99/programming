
import os

##print('Your file will be stored in directory', os.getcwd())
##
##fruits = open('fruits.txt', 'w')
##fruits.write('Apples\n')
##print(fruits.tell())
##fruits.write('Mangos\n')
##fruits.close()

# Case 1: read file using readline() statements:
##fruits = open('fruits.txt', 'r' )
##line_1 = fruits.readline()
##print(line_1)
##line_2 = fruits.readline()
##print(line_2)
##fruits.close()

# Case 2: read file from while-loop:
##fruits = open('fruits.txt', 'r')
##
##line = fruits.readline()
##while line != '':
##  print(line[:-1])
##  line = fruits.readline()
##
##fruits.close()

# Case 3: read file from for-loop:
##fruits = open('fruits.txt', 'r')
##for line in fruits:
##  print(line[:-1])
##fruits.close()

#
# Re-setting the file-pointer:
#
##fruits = open('fruits.txt', 'r')
##for line in fruits:
##  print(line[:-1])
##fruits.seek(0)
##for line in fruits:
##  print(line[:-1])
##fruits.close()


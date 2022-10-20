
import os

##print('Your file will be stored in directory',os.getcwd())
######
##fruits = open('fruits.txt', 'a')
##fruits.write('Apples\n')
##print('file-pointer position:', fruits.tell())
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

#
# Searching, dissecting and constructing strings:
#
##email = 's_park@naver.com'
##at_index = email.find('@')
##user = email[0:at_index]
##domain = email[at_index + 1:]
##print(user, domain)

#
# Unhandled ZeroDivision Exception:
#
##numSuccesses = 10
##numFailures = int(input('failures: '))
##
##successFailureRatio = numSuccesses / numFailures
##print('The success/failure ratio is', successFailureRatio)
##print('Now here')

#
# Handled ZeroDivision Exception:
#
##numSuccesses = 10
##numFailures = int(input('failures: '))
##try:
##  successFailureRatio = numSuccesses / numFailures
##  print('The success/failure ratio is', successFailureRatio)
##except ZeroDivisionError:
##  print('Division by zero exception occurred!')
##  print('successFailureRatio is undefined!')
##print('Now here')


#
# Handling specific exceptions:
#
##try:
##  x = int(input('First number: '))
##  y = int(input('Second number: '))
##  print('x/y = ', x/y)
##  print('x+y = ', x + y)
##  print(xyz) # Name error
##except ValueError:
##  print('Could not convert to number.')
##except ZeroDivisionError:
##  print("Can't divide by zero.")
##except:
##  print('Something else went wrong.')

#
# Input-loop controlled by Boolean flag:
#
##ValidInput = False
##while not ValidInput:
##  val = input('Enter an integer: ')
##  try:
##    val = int(val)
##    print('The square of your number is ', val**2)
##    ValidInput = True # exit loop
##  except ValueError:
##    print(val, 'is not an integer')
##
##print('Good bye...')

#
# Input-loop abstracted away inside function:
# (To reduce code-bloat.)
#
##def readInt():
##  while True:
##    val = input('Enter an integer: ')
##    try:
##      val = int(val)
##      return val 
##    except ValueError:
##      print(val, 'is not an integer')
##
##x = readInt()
##y = readInt()
##print(x**y)

#
# Polymorphic input function:
# (To reduce code-bloat.)
#
##def readVal(valType, requestMsg, errorMsg):
##  while True:
##    val = input(requestMsg)
##    try:
##      val = valType(val)
##      return val
##    except ValueError:
##      print(val, errorMsg)
##
##x = readVal(int, 'Enter an integer: ', 'not an integer')
##y = readVal(float, 'Enter a float: ', 'not a float')
##print(x, y)

#
# Propagation of a raised exception:
#
##import math
##
##def poorRead():
##  return int(input('Enter an integer: '))
##
##def computeCircleArea():
##  r = poorRead()
##  area = r**2 * math.pi
##  print('Result:', area)
##
##print("Let's compute a circle's area")
##try:
##  computeCircleArea()
##except ValueError:
##  print('Invalid computation, good bye...')


#
# Throwing exception back to function caller:
#
##def getRatios(vec1, vec2):
##  """Assumes: vec1 and vec1 are lsits of queal length of numbers
##     Returns: a list containing the meaningful values of
##              vec1[i] / vec2[i]"""
##  ratios = []
##  for index in range(len(vec1)):
##    try:
##      ratios.append(vec1[index] / vec2[index])
##    except ZeroDivisionError:
##      ratios.append(float('nan')) #nan = Not a Number
##    except: #all other exceptions (default handler)
##      raise ValueError('getRatios bad arguments!')
##  return ratios
##
##l1 = [1.0, 2.0, 7.0, 6.0]
##l2 = [1.0, 2.0, 0.0, 3.0]
##try:
##  print(getRatios(l1, l2))
##  print(getRatios([], []))
##  print(getRatios([1,2], [3]))
##except ValueError as msg: # assign exception to 'msg' variable
##  print(msg)
##  print(type(msg))




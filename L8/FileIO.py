input_file_opened = False

while not input_file_opened:
  file_name = input('Enter file name: ')
  try:
    input_file = open(file_name, 'r')
    input_file_opened = True # Get here only if 'open' succeeded!
  except IOError:
    print('Error: file could not be opened.')

line = input_file.readline() 
while line != '':
  print(line.strip('\n'))
  line = input_file.readline()

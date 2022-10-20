# Sparse Text Program

def createModifiedFile(input_file, outputfile):
    '''
        For text file input_file, creates a new version in file outputfile
        in which all instances of the letter 'e' are removed.
    '''
    
    empty_str = ''
    num_total_chars = 0
    num_removals = 0

    for line in input_file:
    
        # save original line length
        orig_line_length = len(line) - 1
       
        
        # remove all occurrances of letter 'e'
        modified_line = line.replace('e',empty_str).replace('E',empty_str)\
                        .replace('a',empty_str).replace('A',empty_str)\
                        .replace('i',empty_str).replace('I',empty_str)\
                        .replace('o',empty_str).replace('O',empty_str)\
                        .replace('u',empty_str).replace('U',empty_str)
        num_removals = num_removals + \
                         (orig_line_length - (len(modified_line)-1))

        # simulataneouly output line to screen and output file
        print(modified_line.strip('\n'))
        output_file.write(modified_line)

    return (num_total_chars, num_removals)

# --- main

# open files for reading and writing
file_name = input('Enter file name (including file extension): ')
input_file = open(file_name,'r')
new_file_name = 'new_' + file_name
output_file = open(new_file_name,'w')

# create file with all letter e removed
print()
num_total_chars, num_removals = createModifiedFile(input_file, output_file)

# close current input and output files
input_file.close()
output_file.close()

# display percentage of characters removed
print()
print(num_removals, "vowels removed")
print(num_removals, "out of", num_total_chars, "characters removed")
print('Percentage of data lost:',
      int((num_removals / num_total_chars) * 100), '%')
print('Modified text in file', new_file_name)
    

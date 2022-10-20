# Smoking/Cancer Correlation Program

import math

def openFiles():
    '''
        Prompts the user for the file names to open, opens the files,
        and returns the file objects for each in a tuple of the form
        (air_datafile, cancer_datafile).

        Raises an IOError exception if the files are not successfully
        opened after four attempts of entering file names.
    '''

    # init
    air_datafile_opened = False
    cancer_datafile_opened = False
    num_attempts = 4
    
    # prompt for file names and attempt to open files
    while ((not air_datafile_opened) or \
           (not cancer_datafile_opened)) \
            and (num_attempts > 0):
        try:

            if not cancer_datafile_opened:
                file_name = input('Enter lung cancer data from file name: ')
                cancer_datafile = open(file_name, 'r')
                cancer_datafile_opened = True
                
            if not air_datafile_opened:
                file_name = input('Enter air pollution data from file name: ')
                air_datafile = open(file_name, 'r')
                air_datafile_opened = True
            
        except IOError:
            print('File not found:',file_name + '.','Please reenter\n')
            
            num_attempts = num_attempts - 1

    # if one of more file not opened, raise IOError exception
    if not air_datafile_opened or not cancer_datafile_opened:
        raise IOError('Too many attempts of reading input files')
    
    # return file objects if successfully opened
    else:
        return (air_datafile, cancer_datafile)

def readFiles(air_datafile, cancer_datafile):
    '''
        Reads the data from the provided file objects air_datafile
        and cancer_datafile. Returns a list of the data read from each
        in a tuple of the form (air_datafile, cancer_datafile).
    '''

    # init
    air_data = []
    cancer_data = []
    empty_str = ''

    # read past file headers
    air_datafile.readline()
    cancer_datafile.readline()

    # read data files
    eof = False
    #Add to the list according to the criteria given
    while not eof:
        
        # read line of data from each file
        a_line = air_datafile.readline()
        c_line = cancer_datafile.readline()

        # check if at end-of-file of both files
        if a_line == empty_str and c_line == empty_str:
            eof = True
            
        # check if end of air data file only
        elif a_line == empty_str and c_line != empty_str:
            cancer_data.append(c_line.strip().split(','))
                        
        # check if at end of cancer data file only
        elif c_line == empty_str and c_line != empty_str:
            air_data.append(a_line.strip().split(','))

        # append line of data to each list
        else:
            air_data.append(a_line.strip().split(','))
            cancer_data.append(c_line.strip().split(','))

    #Reconstruct the list to the given conditions
    air_data_real=[]
    cancer_data_real=[]
    
    if len(air_data)>=len(cancer_data):
        for i in range(0,len(air_data)):
            for e in range(0,len(cancer_data)):
                if air_data[i][0].lower()==cancer_data[e][0].lower():
                    air_data_real.append(air_data[i])
                    cancer_data_real.append(cancer_data[e])
    else:
         for i in range(0,len(cancer_data)):
            for e in range(0,len(air_data)):
                if air_data[i][0].lower()==cancer_data[e][0].lower():
                    air_data_real.append(air_data[i])
                    cancer_data_real.append(cancer_data[e])
            
    # return list of data from each file
    return (air_data_real, cancer_data_real)
        
def calculateCorrelation(air_data, cancer_data):
    '''
        Calculates and returns the correlation value for the data
        provided in lists air_pollution_data and cancer_data
    '''    

    # init
    sum_air_vals = sum_cancer_vals = 0
    sum_air_sqrd = sum_cancer_sqrd = 0
    sum_products = 0

    # calculate intermediate correlation values
    num_values = len(air_data)
    
    for k in range(0,num_values):
        
        sum_air_vals = sum_air_vals + float(air_data[k][1])
        sum_cancer_vals = sum_cancer_vals + float(cancer_data[k][1])

        sum_air_sqrd = sum_air_sqrd +  \
                              float(air_data[k][1]) ** 2
        sum_cancer_sqrd = sum_cancer_sqrd +  \
                              float(cancer_data[k][1]) ** 2

        sum_products = sum_products + float(air_data[k][1]) *  \
                       float(cancer_data[k][1])

    # calculate and display correlation value
    numer = (num_values * sum_products) - \
            (sum_air_vals * sum_cancer_vals)

    denom = math.sqrt(abs( \
        ((num_values * sum_air_sqrd) - (sum_air_vals ** 2)) * \
        ((num_values * sum_cancer_sqrd) - (sum_cancer_vals ** 2)) \
        ))
       
    return numer / denom

# ---- main

# program greeting
print ('This program will determine the correlation (-1 to 1) between')
print ('data on cigarette air_pollution and incidences of lung cancer\n')

try:
    # open data files    
    air_datafile, cancer_datafile = openFiles()

    # read data
    air_data, cancer_data = readFiles(air_datafile, cancer_datafile)

    # calculate correlation value
    correlation = calculateCorrelation(air_data, cancer_data)

    # display correlation value
    print ('r_value = ', correlation)

except IOError as e:
    print(str(e))
    print('Program terminated ...')

    

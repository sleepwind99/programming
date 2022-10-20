#######################################################################
#                                                                     #
#  Simple python "judge" GUI for determinstic program output/inputs.  #
#                        By Chansol Yang                              #
#                                                                     #
#                                                                     #
#             Code Spaghetti Index: 7/10 - Quite spaghetti            #
#                                                                     #
#                                                                     #
#  This program is extensively commented;                             #
#  Either with class/method docstrings or with comments.              #
#  Enjoy.                                                             #
#                                                                     #
#######################################################################

dev = False
app_version = "v0.6.2"
db_version = "Lab 12 v2"

db_str = r'''
#### BEGIN AUTO-GENERATED CODE ####

database={}
temp_interactions=[]
temp_interaction=Interaction(interaction_type='INTERACTIVE', command=None, end_command=None, wait_seconds=1, name='Normal use case')
temp_interaction.add_out('')
temp_interaction.add_in_raw('test_dict={}\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('return_value=addDailyTemp(test_dict,"Monday",100)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('sorted(test_dict.items())\n')
temp_interaction.add_out("[('Monday', 100)]\n")
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type='INTERACTIVE', command=None, end_command=None, wait_seconds=1, name='Return values')
temp_interaction.add_out('')
temp_interaction.add_in_raw('test_dict={}\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('return_value=addDailyTemp(test_dict,"Monday",100)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('sorted(test_dict.items())\n')
temp_interaction.add_out("[('Monday', 100)]\n")
temp_interaction.add_in_raw('sorted(return_value.items())\n')
temp_interaction.add_out("[('Monday', 100)]\n")
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type='INTERACTIVE', command=None, end_command=None, wait_seconds=1, name='Non-empty lists')
temp_interaction.add_out('')
temp_interaction.add_in_raw('test_dict={"Sunday":50}\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('return_value=addDailyTemp(test_dict,"Monday",100)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('sorted(test_dict.items())\n')
temp_interaction.add_out("[('Monday', 100), ('Sunday', 50)]\n")
temp_interaction.add_in_raw('sorted(return_value.items())\n')
temp_interaction.add_out("[('Monday', 100), ('Sunday', 50)]\n")
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type='INTERACTIVE', command=None, end_command=None, wait_seconds=1, name='Name clash')
temp_interaction.add_out('')
temp_interaction.add_in_raw('test_dict={"Sunday":50,"Monday":70}\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('return_value=addDailyTemp(test_dict,"Monday",100)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('sorted(test_dict.items())\n')
temp_interaction.add_out("[('Monday', 70), ('Sunday', 50)]\n")
temp_interaction.add_in_raw('sorted(return_value.items())\n')
temp_interaction.add_out("[('Monday', 70), ('Sunday', 50)]\n")
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type='INTERACTIVE', command=None, end_command=None, wait_seconds=1, name='Multiple calls')
temp_interaction.add_out('')
temp_interaction.add_in_raw('test_dict={"Sunday":50,"Monday":70}\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('return_value=addDailyTemp(test_dict,"Thursday",10)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('sorted(test_dict.items())\n')
temp_interaction.add_out("[('Monday', 70), ('Sunday', 50), ('Thursday', 10)]\n")
temp_interaction.add_in_raw('sorted(return_value.items())\n')
temp_interaction.add_out("[('Monday', 70), ('Sunday', 50), ('Thursday', 10)]\n")
temp_interaction.add_in_raw('return_value=addDailyTemp(test_dict,"Wednesday",30)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('sorted(test_dict.items())\n')
temp_interaction.add_out("[('Monday', 70), ('Sunday', 50), ('Thursday', 10), ('Wednesday', 30)]\n")
temp_interaction.add_in_raw('sorted(return_value.items())\n')
temp_interaction.add_out("[('Monday', 70), ('Sunday', 50), ('Thursday', 10), ('Wednesday', 30)]\n")
temp_interaction.add_in_raw('return_value=addDailyTemp(test_dict,"Monday",100)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('sorted(test_dict.items())\n')
temp_interaction.add_out("[('Monday', 70), ('Sunday', 50), ('Thursday', 10), ('Wednesday', 30)]\n")
temp_interaction.add_in_raw('sorted(return_value.items())\n')
temp_interaction.add_out("[('Monday', 70), ('Sunday', 50), ('Thursday', 10), ('Wednesday', 30)]\n")
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type='INTERACTIVE', command=None, end_command=None, wait_seconds=1, name='Non-string values')
temp_interaction.add_out('')
temp_interaction.add_in_raw('test_dict={"Sunday":50,-1:100}\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('hell=5\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('return_value=addDailyTemp(test_dict,hell,"Hot as hell")\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('sorted(test_dict.items(),key=str)\n')
temp_interaction.add_out("[('Sunday', 50), (-1, 100), (5, 'Hot as hell')]\n")
temp_interaction.add_in_raw('sorted(return_value.items(),key=str)\n')
temp_interaction.add_out("[('Sunday', 50), (-1, 100), (5, 'Hot as hell')]\n")
temp_interaction.add_in_raw('return_value=addDailyTemp(test_dict,(4,5),1234)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('sorted(test_dict.items(),key=str)\n')
temp_interaction.add_out("[('Sunday', 50), ((4, 5), 1234), (-1, 100), (5, 'Hot as hell')]\n")
temp_interaction.add_in_raw('sorted(return_value.items(),key=str)\n')
temp_interaction.add_out("[('Sunday', 50), ((4, 5), 1234), (-1, 100), (5, 'Hot as hell')]\n")
temp_interactions.append(temp_interaction)
database['Problem 1']=temp_interactions
temp_interactions=[]
temp_interaction=Interaction(interaction_type='INTERACTIVE', command=None, end_command=None, wait_seconds=1, name='Normal use case')
temp_interaction.add_out('')
temp_interaction.add_in_raw('test_dict={"Sun":75,"Mon":73,"Tue":60,"Wed":100,"Thu":78,"Fri":20,"Sat":-10}\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('result=moderateDays(test_dict)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('result.sort()\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('result\n')
temp_interaction.add_out("['Mon', 'Sun', 'Thu']\n")
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type='INTERACTIVE', command=None, end_command=None, wait_seconds=1, name='Inclusive range')
temp_interaction.add_out('')
temp_interaction.add_in_raw('test_dict={"Sun":69,"Mon":70,"Tue":71,"Wed":78,"Thu":79,"Fri":80,"Sat":10}\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('result=moderateDays(test_dict)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('result.sort()\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('result\n')
temp_interaction.add_out("['Mon', 'Thu', 'Tue', 'Wed']\n")
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type='INTERACTIVE', command=None, end_command=None, wait_seconds=1, name='Empty result')
temp_interaction.add_out('')
temp_interaction.add_in_raw('test_dict={"Sun":0,"Mon":10,"Tue":20,"Wed":45,"Thu":100,"Fri":46,"Sat":10}\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('result=moderateDays(test_dict)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('result.sort()\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('result\n')
temp_interaction.add_out('[]\n')
temp_interactions.append(temp_interaction)
database['Problem 2']=temp_interactions
temp_interactions=[]
temp_interaction=Interaction(interaction_type='CONSOLE COMMAND', command="lambda py_path,py_directory: file_writer(py_path, py_directory, 'CPChecker_L12P3T1.txt', L12P3T1)", end_command=None, wait_seconds=1, name='Set 1 - Encryption')
temp_interaction.add_out('Enter a filename: ')
temp_interaction.add_in_raw('CPChecker_L12P3T1.txt\n')
temp_interaction.add_out('')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type='INTERACTIVE EXTENDED NOEXEC', command=None, end_command=None, wait_seconds=1, name='Set 1 - Key coverage')
temp_interaction.add_out('')
temp_interaction.add_in_raw('# Checking if all values from a-z, A-Z, 0-9, and space is included\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw("csv_map=CPChecker.L12.paired_csv_parse(csv_file='CPChecker_L12P3T1.key')\n")
temp_interaction.add_out('')
temp_interaction.add_in_raw('sorted(csv_map.keys())\n')
temp_interaction.add_out("[' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']\n")
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type='INTERACTIVE EXTENDED NOEXEC', command=None, end_command=None, wait_seconds=1, name='Set 1 - Decryption(CPChecker)')
temp_interaction.add_out('')
temp_interaction.add_in_raw(
    '# Decrypting with the internal program.\n'+
    '# If this fails, it means your encryption algorithm is wrong.\n'+
    ''
    )
temp_interaction.add_out('')
temp_interaction.add_in_raw("CPChecker.L12.decrypt(keyfile='CPChecker_L12P3T1.key',encryptfile='CPChecker_L12P3T1.enc')\n")
temp_interaction.add_out(
    'CPChecker decrypted your file with the given .key.\n'+
    'Decryption results:\n'+
    'Hello World\n'+
    '\n'+
    ''
    )
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type='CONSOLE COMMAND', command=None, end_command="lambda py_path,py_directory: file_deleter(py_path, py_directory, 'CPChecker_L12P3T1.enc')+'\\n'+file_deleter(py_path, py_directory, 'CPChecker_L12P3T1.key')+'\\n'+file_deleter(py_path, py_directory, 'CPChecker_L12P3T1.txt')", wait_seconds=1, name='Set 1 - Decryption(Your program)')
temp_interaction.add_out('Enter a filename: ')
temp_interaction.add_in_raw('CPChecker_L12P3T1.enc\n')
temp_interaction.add_out('')
temp_interaction.add_text( 'CPChecker_L12P3T1.txt' ,'Hello World\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type='CONSOLE COMMAND', command="lambda py_path,py_directory: file_writer(py_path, py_directory, 'CPChecker_L12P3T1.txt', L12P3T2)", end_command=None, wait_seconds=1, name='Set 2 - Encryption')
temp_interaction.add_out('Enter a filename: ')
temp_interaction.add_in_raw('CPChecker_L12P3T1.txt\n')
temp_interaction.add_out('')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type='INTERACTIVE EXTENDED NOEXEC', command=None, end_command=None, wait_seconds=1, name='Set 2 - Decryption(CPChecker)')
temp_interaction.add_out('')
temp_interaction.add_in_raw(
    '# Decrypting with the internal program.\n'+
    '# If this fails, it means your encryption algorithm is wrong.\n'+
    ''
    )
temp_interaction.add_out('')
temp_interaction.add_in_raw("CPChecker.L12.decrypt(keyfile='CPChecker_L12P3T1.key',encryptfile='CPChecker_L12P3T1.enc')\n")
temp_interaction.add_out(
    'CPChecker decrypted your file with the given .key.\n'+
    'Decryption results:\n'+
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 \n'+
    '\n'+
    ''
    )
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type='CONSOLE COMMAND', command=None, end_command="lambda py_path,py_directory: file_deleter(py_path, py_directory, 'CPChecker_L12P3T1.enc')+'\\n'+file_deleter(py_path, py_directory, 'CPChecker_L12P3T1.key')+'\\n'+file_deleter(py_path, py_directory, 'CPChecker_L12P3T1.txt')", wait_seconds=1, name='Set 2 - Decryption(Your program)')
temp_interaction.add_out('Enter a filename: ')
temp_interaction.add_in_raw('CPChecker_L12P3T1.enc\n')
temp_interaction.add_out('')
temp_interaction.add_text( 'CPChecker_L12P3T1.txt' ,'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 \n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type='CONSOLE COMMAND', command="lambda py_path,py_directory: file_writer(py_path, py_directory, 'CPChecker_L12P3T1.txt', L12P3T3)", end_command=None, wait_seconds=1, name='Set 3 - Encryption')
temp_interaction.add_out('Enter a filename: ')
temp_interaction.add_in_raw('CPChecker_L12P3T1.txt\n')
temp_interaction.add_out('')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type='INTERACTIVE EXTENDED NOEXEC', command=None, end_command=None, wait_seconds=1, name='Set 3 - Decryption(CPChecker)')
temp_interaction.add_out('')
temp_interaction.add_in_raw(
    '# Decrypting with the internal program.\n'+
    '# If this fails, it means your encryption algorithm is wrong.\n'+
    ''
    )
temp_interaction.add_out('')
temp_interaction.add_in_raw("CPChecker.L12.decrypt(keyfile='CPChecker_L12P3T1.key',encryptfile='CPChecker_L12P3T1.enc')\n")
temp_interaction.add_out(
    'CPChecker decrypted your file with the given .key.\n'+
    'Decryption results:\n'+
    'Hello there\n'+
    'This is a simple text\n'+
    'I dont know what to write here\n'+
    'I cant even use punctuation marks man\n'+
    'help\n'+
    '\n'+
    ''
    )
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type='CONSOLE COMMAND', command=None, end_command="lambda py_path,py_directory: file_deleter(py_path, py_directory, 'CPChecker_L12P3T1.enc')+'\\n'+file_deleter(py_path, py_directory, 'CPChecker_L12P3T1.key')+'\\n'+file_deleter(py_path, py_directory, 'CPChecker_L12P3T1.txt')", wait_seconds=1, name='Set 3 - Decryption(Your program)')
temp_interaction.add_out('Enter a filename: ')
temp_interaction.add_in_raw('CPChecker_L12P3T1.enc\n')
temp_interaction.add_out('')
temp_interaction.add_text( 'CPChecker_L12P3T1.txt' ,
    'Hello there\n'+
    'This is a simple text\n'+
    'I dont know what to write here\n'+
    'I cant even use punctuation marks man\n'+
    'help\n'+
    ''
    )
temp_interactions.append(temp_interaction)
database['Problem 3']=temp_interactions
temp_interactions=[]
temp_interaction=Interaction(interaction_type='CONSOLE', command=None, end_command=None, wait_seconds=1, name='Minty')
temp_interaction.add_out('Enter a color: ')
temp_interaction.add_in_raw('3eefab\n')
temp_interaction.add_out(
    'Red: 62\n'+
    'Green: 239\n'+
    'Blue: 171\n'+
    ''
    )
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type='CONSOLE', command=None, end_command=None, wait_seconds=1, name='Pink')
temp_interaction.add_out('Enter a color: ')
temp_interaction.add_in_raw('ff3a8f\n')
temp_interaction.add_out(
    'Red: 255\n'+
    'Green: 58\n'+
    'Blue: 143\n'+
    ''
    )
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type='CONSOLE', command=None, end_command=None, wait_seconds=1, name='Deep green')
temp_interaction.add_out('Enter a color: ')
temp_interaction.add_in_raw('2a720b\n')
temp_interaction.add_out(
    'Red: 42\n'+
    'Green: 114\n'+
    'Blue: 11\n'+
    ''
    )
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type='CONSOLE', command=None, end_command=None, wait_seconds=1, name='My favorite color')
temp_interaction.add_out('Enter a color: ')
temp_interaction.add_in_raw('cc9cdf\n')
temp_interaction.add_out(
    'Red: 204\n'+
    'Green: 156\n'+
    'Blue: 223\n'+
    ''
    )
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type='CONSOLE', command=None, end_command=None, wait_seconds=1, name='Black')
temp_interaction.add_out('Enter a color: ')
temp_interaction.add_in_raw('000000\n')
temp_interaction.add_out(
    'Red: 0\n'+
    'Green: 0\n'+
    'Blue: 0\n'+
    ''
    )
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type='CONSOLE', command=None, end_command=None, wait_seconds=1, name='White')
temp_interaction.add_out('Enter a color: ')
temp_interaction.add_in_raw('ffffff\n')
temp_interaction.add_out(
    'Red: 255\n'+
    'Green: 255\n'+
    'Blue: 255\n'+
    ''
    )
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type='CONSOLE', command=None, end_command=None, wait_seconds=1, name='Capitalization')
temp_interaction.add_out('Enter a color: ')
temp_interaction.add_in_raw('3EefAB\n')
temp_interaction.add_out(
    'Red: 62\n'+
    'Green: 239\n'+
    'Blue: 171\n'+
    ''
    )
temp_interactions.append(temp_interaction)
database['Problem 4']=temp_interactions
temp_interactions=[]
temp_interaction=Interaction(interaction_type='INTERACTIVE', command=None, end_command=None, wait_seconds=1, name='Constructor/repr')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f=Fraction(14,21)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f.getNumerator()\n')
temp_interaction.add_out('2\n')
temp_interaction.add_in_raw('f.getDenominator()\n')
temp_interaction.add_out('3\n')
temp_interaction.add_in_raw('str(f)\n')
temp_interaction.add_out("'2/3'\n")
temp_interaction.add_in_raw('repr(f)\n')
temp_interaction.add_out("'2/3'\n")
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type='INTERACTIVE', command=None, end_command=None, wait_seconds=1, name='Getter/Setter')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f=Fraction(1,2)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f.getNumerator()\n')
temp_interaction.add_out('1\n')
temp_interaction.add_in_raw('f.getDenominator()\n')
temp_interaction.add_out('2\n')
temp_interaction.add_in_raw('f.setNumerator(3)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f.setDenominator(6)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f.getNumerator()\n')
temp_interaction.add_out('3\n')
temp_interaction.add_in_raw('f.getDenominator()\n')
temp_interaction.add_out('6\n')
temp_interaction.add_in_raw('f\n')
temp_interaction.add_out('3/6\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type='INTERACTIVE', command=None, end_command=None, wait_seconds=1, name='Getter/Setter (zeroes)')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f=Fraction(1,2)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f.getNumerator()\n')
temp_interaction.add_out('1\n')
temp_interaction.add_in_raw('f.getDenominator()\n')
temp_interaction.add_out('2\n')
temp_interaction.add_in_raw('f.setNumerator(0)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw(
    'try:\n'+
    '    f.setDenominator(0)\n'+
    "    err='No error'\n"+
    'except ValueError as e:\n'+
    '    err=e\n'+
    ''
    )
temp_interaction.add_out('')
temp_interaction.add_in_raw('err\n')
temp_interaction.add_out("ValueError('Divide by Zero Error',)\n")
temp_interaction.add_in_raw('f.getNumerator()\n')
temp_interaction.add_out('0\n')
temp_interaction.add_in_raw('f.getDenominator()\n')
temp_interaction.add_out('2\n')
temp_interaction.add_in_raw('f\n')
temp_interaction.add_out('0/2\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type='INTERACTIVE', command=None, end_command=None, wait_seconds=1, name='Copy')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f=Fraction(1,2)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f2=f.copy()\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f.setNumerator(3)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f.setDenominator(6)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f\n')
temp_interaction.add_out('3/6\n')
temp_interaction.add_in_raw('f2\n')
temp_interaction.add_out('1/2\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type='INTERACTIVE', command=None, end_command=None, wait_seconds=1, name='Copy (Reduce)')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f=Fraction(1,2)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f.setNumerator(3)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f.setDenominator(6)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f2=f.copy()\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f\n')
temp_interaction.add_out('3/6\n')
temp_interaction.add_in_raw('f2\n')
temp_interaction.add_out('3/6\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type='INTERACTIVE', command=None, end_command=None, wait_seconds=1, name='Reduce')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f=Fraction(1,2)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f.setNumerator(3)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f.setDenominator(7)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f.reduce()\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f\n')
temp_interaction.add_out('3/7\n')
temp_interaction.add_in_raw('f.setNumerator(3)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f.setDenominator(6)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f.reduce()\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f\n')
temp_interaction.add_out('1/2\n')
temp_interaction.add_in_raw('f.setNumerator(3753*534)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f.setDenominator(3753*133)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f.reduce()\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f\n')
temp_interaction.add_out('534/133\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type='INTERACTIVE', command=None, end_command=None, wait_seconds=1, name='Adjust')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f=Fraction(1,2)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f.adjust(2)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f\n')
temp_interaction.add_out('2/4\n')
temp_interaction.add_in_raw('f.setNumerator(3)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f.setDenominator(6)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f.adjust(2)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f\n')
temp_interaction.add_out('6/12\n')
temp_interaction.add_in_raw('f.adjust(10)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f\n')
temp_interaction.add_out('60/120\n')
temp_interactions.append(temp_interaction)
temp_interaction=Interaction(interaction_type='INTERACTIVE', command=None, end_command=None, wait_seconds=1, name='Negative Fractions')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f=Fraction(1,2)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f.setNumerator(-3)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f.setDenominator(6)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f.reduce()\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f # Note: 1/-2 is also correct.\n')
temp_interaction.add_out('-1/2\n')
temp_interaction.add_in_raw('f.setNumerator(3)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f.setDenominator(-6)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f.reduce()\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f # Note: -1/2 is also correct.\n')
temp_interaction.add_out('1/-2\n')
temp_interaction.add_in_raw('f.setNumerator(-3)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f.setDenominator(-6)\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f.reduce()\n')
temp_interaction.add_out('')
temp_interaction.add_in_raw('f\n')
temp_interaction.add_out('1/2\n')
temp_interactions.append(temp_interaction)
database['Problem 5']=temp_interactions

##### END AUTO-GENERATED CODE #####
'''


## Below is a code that will attatch a custom error handler
## So the console won't close on its own when an uncaught exception happens.
## Makes for easy debugging.
if __name__ == "__main__":
    import sys
    import traceback


    ## This will make it so the console won't close on its own when an exception is raised.
    def show_exception_and_exit(exc_type, exc_value, tb):
        if not str(exc_value) == 'name \'exit\' is not defined':
            print("\n\n---ERROR---\n")
            traceback.print_exception(exc_type, exc_value, tb)
            input("\nPress any key to exit.")
        sys.exit(-1)


    sys.excepthook = show_exception_and_exit

## Imports
import subprocess  # For spawning a seperate python process
import io  # For interacting with that process
import sys  # To get the system encoding used
import webbrowser  # For a web URL link in the UI.
import traceback  # Error tracebacks
import os.path  # File path manipulation
import os  # change cwd and remove files
import time  # for timekeeping

## Tkinter imports.
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog


def dict_print(d):
    for i in d:
        print(i, ":", repr(d[i]))


def debug_print(g, l):
    print("--------DEBUG---------")
    print("----[Globals]----")
    dict_print(g)
    print("----[Locals]----")
    dict_print(l)


class InvalidInternalStateError(Exception):
    pass


class SliderPlus(Frame):
    '''Slider with a label and a value display.
    Optionally takes these keyword argumemts:
    plus_name, plus_max,plus_min,plus_divisions,plus_format
    '''

    def __init__(self, *args, plus_name="NoName", plus_max=100, plus_min=0, plus_divisions=100, plus_format=2,
                 plus_display_override=None, plus_callback=None, **kwargs):
        # Variables
        self._plus_name = plus_name
        self._plus_max = plus_max
        self._plus_min = plus_min
        self._plus_divisions = plus_divisions
        self._plus_format = plus_format
        self._plus_value = self._plus_min
        self._plus_callback = plus_callback

        self._plus_display_override = plus_display_override

        super().__init__(**kwargs)

        # Label
        self._plus_label = Label(self, text=self._plus_name)
        self._plus_label.grid(row=1, column=1)

        # Slider
        self._plus_slider = Scale(self, orient=HORIZONTAL, length=200, from_=0, to=self._plus_divisions, value=0,
                                  command=self._plus_slider_changed)
        self._plus_slider.grid(column=2, row=1, padx=5, sticky=(W, E))
        self.columnconfigure(2, weight=1)
        self._plus_slider.bind("<ButtonRelease>", self._slider_released)
        self.columnconfigure(2, weight=1)
        # Value
        self._plus_value_str_label = Label(self, text=str(self._plus_min))
        self._plus_value_str_label.grid(column=3, row=1, sticky=(W, E))

        self._plus_slider_changed(self._plus_min)

    def _slider_released(self, evt):
        pass

    def _plus_slider_changed(self, x):
        self._plus_value = int(round(float(x))) / self._plus_divisions * (
            self._plus_max - self._plus_min) + self._plus_min
        if self._plus_display_override == None:
            self._plus_value_str_label.configure(text=("{:." + str(self._plus_format) + "f}").format(self._plus_value))
        else:
            self._plus_value_str_label.configure(text=self._plus_display_override(self._plus_value))

        if self._plus_callback is not None:
            self._plus_callback(self.plus_get_value())

    def plus_set(self, val):
        self._plus_slider.set(int(self._plus_divisions * (val - self._plus_min) / (self._plus_max - self._plus_min)))

    def plus_get_value(self):
        return self._plus_value


class CodePanel(LabelFrame):
    '''
    A Tk widget for displaying program outputs.
    It provides an easy way to display multiple lines of interactive code.
    This class inherits from a ttk.LabelFrame and can be used just like any other tk widget.
    '''

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self._container = Frame(self)
        self._container.grid(row=1, column=1, padx=5, pady=5, sticky=(N, S, E, W))
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        self._code_area = Text(self._container, font=("Consolas", 10), width=60, relief=RIDGE, borderwidth=2)
        self._code_area.grid(row=1, column=1, sticky=(N, S, E, W))
        self._container.columnconfigure(1, weight=1)
        self._container.rowconfigure(1, weight=1)

        self._code_area.tag_config("out", foreground="black")
        self._code_area.tag_config("in", foreground="blue")
        self._code_area.tag_config("err", foreground="red")
        self._code_area.tag_config("exec", foreground="green")
        self._code_area.tag_config("system", foreground="purple")
        self._code_area.tag_config("wrong", background="#FBB")
        self._code_area.configure(state='disabled')

        self._scrollbar = Scrollbar(self._container, command=self._code_area.yview)
        self._scrollbar.grid(row=1, column=2, sticky=(N, S, E, W))

        self._code_area['yscrollcommand'] = self._scrollbar.set

    def new_in(self, s):
        '''
        Append a given input string (usually stdin).
        It will show up as a blue text.
        '''

        self._code_area.configure(state='normal')
        self._code_area.insert("end", s, ("in",))
        self._code_area.configure(state='disabled')

        self._code_area.see(END)

    def new_out(self, s, highlight=None):
        '''
        Append a given output string (usually stdout).
        It will show up as a plain black text.

        An optional list of character indices to highlight can be provided;
        For example, passing (0,1) will highlight the first and second characters red.
        Used for marking wrong answers.
        '''

        if highlight == None:
            to_highlight = []
        else:
            to_highlight = list(highlight)

        self._code_area.configure(state='normal')
        for idx in range(len(s)):
            tag = ("out",)
            if idx in to_highlight:
                tag = ("wrong",)
            self._code_area.insert("end", s[idx], tag)
        self._code_area.configure(state='disabled')

        self._code_area.see(END)

    def new_err(self, s):
        '''
        Append a given error string (usually stderr).
        It will show up as a red text.
        '''

        self._code_area.configure(state='normal')
        self._code_area.insert("end", s, ("err",))
        self._code_area.configure(state='disabled')

        self._code_area.see(END)

    def new_exec(self, s):
        '''
        Append a given error string (usually stderr).
        It will show up as a red text.
        '''

        if s[-1]=="\n":
            s=s[:-1]

        self._code_area.configure(state='normal')
        self._code_area.insert("end", ">>> " + "\n... ".join(s.split("\n"))+"\n", ("exec",))
        self._code_area.configure(state='disabled')

        self._code_area.see(END)

    def new_system(self, s):
        '''
        Append a given error string (usually stderr).
        It will show up as a red text.
        '''

        self._code_area.configure(state='normal')
        self._code_area.insert("end", s, ("system",))
        self._code_area.configure(state='disabled')

        self._code_area.see(END)

    def clear(self):
        '''
        Clear all text.
        '''
        self._code_area.configure(state='normal')
        self._code_area.delete('1.0', END)
        self._code_area.configure(state='disabled')

    def text_remove(self, chars):
        raise NotImplementedError("Sorry mate. Can't get thgis friggin thing to work.")

        print("Removing", chars, "characters")
        self._code_area.configure(state='normal')
        # self._code_area.insert("end -{} chars".format(chars+1), "[DEL HERE]", ("system",))
        self._code_area.delete("end -{} chars".format(chars + 1), END)

        self._code_area.configure(state='disabled')


class AbstractScript():
    '''
    Base class for script interfaces.
    Not really useful right now, but may become useful if we add support for languages other than Python.
    '''

    def __init__(self):
        pass

    def read(self):
        '''
        Read a program's output from stdout.
        '''
        pass

    def write(self, s):
        '''
        Write a given string to the program's stdin.
        '''
        pass

    def kill(self):
        '''
        Kill and clean up.
        '''
        pass


def stdin_encoding():
    '''
    Gets the encoding of stdin.
    '''
    return get_console_encoding()


def stdout_encoding():
    '''
    Gets the encoding of stdout.
    '''
    return get_console_encoding()


class PythonCommunicationError(Exception):
    '''
    Exception for python interface related error.
    '''
    pass


class PythonScriptError(Exception):
    pass


class PipeEncodingError(Exception):
    '''
    Exception for encoding error in the pipe communication.
    '''
    pass


## InteractivePythonScript's extension code.
## Below code is evaluated before executing the user script.
## Everything is hidden inside the CPChecker class,
## To avoid name collisions.
extension = r"""

import io

class CPChecker():
    current_py_path = {py_path!r}
    current_py_directory = {py_directory!r}

    class PathOps:
        @classmethod
        def path_relative(cls, p):
            try:
                return os.path.relpath(p, start=CPChecker.current_py_directory)
            except:
                return p
        
    class VirtualIO:
        class TestingIO(io.StringIO):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.test_closed = False
                self.test_mode = "FILE NOT OPENED"

            def close(self):
                self.test_closed = True
                
        files = dict()

        @classmethod
        def create_virtual_file(cls, filename, s=''):
            cls.files[filename] = cls.TestingIO(s)

        @classmethod
        def check_file_mode(cls, filename):
            return cls.files[filename].test_mode

        @classmethod
        def check_file_closed(cls, filename):
            return cls.files[filename].test_closed

        @classmethod
        def check_file_contents(cls, filename):
            return cls.files[filename].getvalue()

        @classmethod
        def open(cls, filename, mode='r', *args, **kwargs):
            if filename not in cls.files:
                raise IOError("Cannot find virtual file " + repr(filename))
            target = cls.files[filename]
            target.test_mode = mode
            return target

        @classmethod
        def override_open(cls):
            global open
            open = cls.open
    
    class Print:
        def __init__(self, s):
            self.s = s
            if s == '':
                self.s = '(empty)'

        def __repr__(self):
            return self.s

    class SortedList(list):
        def __repr__(self):
            return "[" + ",\n ".join([repr(i) for i in sorted(self)]) + "]"

    class DefaultedDict(dict):
        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
        def __getitem__(self, item):
            res=None
            try:
                res=super().__getitem__(item)
            except KeyError:
                res=item
            return res
    
    class L12:
        @classmethod
        def paired_csv_parse(cls,*args,csv_file=''):
            with open(csv_file,'r') as f:
                contents=f.read()
            return dict([i.split(',') for i in contents.split('\n') if i])
        @classmethod
        def decrypt(cls,*args,keyfile='',encryptfile=''):
            
            with open(keyfile,'r') as f:
                key_raw=f.read()
            with open(encryptfile, 'r') as f:
                encrypted_raw = f.read()
                
            try:
                mapping = CPChecker.DefaultedDict([i.split(',')[::-1] for i in key_raw.split('\n') if i])
            except TypeError:
                raise Exception("CSV parse failed.")
            
            return CPChecker.Print('CPChecker decrypted your file with the given .key.\nDecryption results:\n'+''.join([mapping[i] for i in encrypted_raw]))

"""





    


class InteractivePythonScript(AbstractScript):
    '''
    Interface for executing a python script, and then testing it using an interactive console.
    Similar of how you would run a module in IDLE, and then go to an interactive console will all the module's
    definitions.
    '''

    def __init__(self, path, extended=False, noexec=False):
        super().__init__()
        self.path = path
        self.out = None
        self.namespace = dict()

        if extended:
            extension_formatted=extension.format(py_path=py_file,py_directory=get_py_directory())
            exec(compile(extension_formatted, "<shell-extension>", "exec"), self.namespace)


        if not noexec:
            with open(path, "r", encoding=get_file_encoding()) as f:
                code = f.read()
            exec(compile(code, "<python-script>", "exec"), self.namespace)

    def read(self):
        if self.out != None:
            tmp = self.out
            self.out = None
            return repr(tmp)
        return ""

    def write(self, s):
        try:
            code = compile(s, "<interactive-shell-multiline>", "exec")
            code = compile(s, "<interactive-shell-single>", "single")
            code = compile(s, "<interactive-shell-eval>", "eval")
        except SyntaxError:
            pass

        self.out = eval(code, self.namespace)


class PythonScript(AbstractScript):
    '''
    An interface for communicating with an external python script.
    
    Provides an easy-to-use interface with an external python script, hiding away all the complications
    that arise when using pipes to communicate between processes.
    '''

    def __init__(self, path):
        super().__init__()
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        try:
            self.p = subprocess.Popen(['py', "-u", path],
                                      stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE,
                                      bufsize=1, startupinfo=startupinfo,
                                      cwd=get_py_directory())
        except:
            raise PythonCommunicationError("Error in starting python script. Did you select a .py file?")

    def read(self):
        '''
        Read from the stdout of the python script.
        
        Please note that read() may not return results when you call it immediately after initializing the object
        or write()-ing, even if the script does in the command line.
        This is due to buffer taking time to flush (I think)
        You should wait (A time.sleep() would work) about 0.5 seconds before attempting to read.
   
        May raise a PythonScriptError;
        This usually indicates that the program has terminated.
        '''
        try:
            self.p.stdout.flush()
            self.p.stdout.seek(0, io.SEEK_END)
            end = self.p.stdout.tell()
            self.p.stdout.seek(0, io.SEEK_SET)
            try:
                res = self.p.stdout.read(end).decode(stdout_encoding()).replace("\r\n", "\n")
            except UnicodeDecodeError:
                raise PipeEncodingError("Decode Failed")

            self.p.stderr.flush()
            self.p.stderr.seek(0, io.SEEK_END)
            end = self.p.stderr.tell()
            self.p.stderr.seek(0, io.SEEK_SET)
            try:
                err = self.p.stderr.read(end).decode(stdout_encoding()).replace("\r\n", "\n")
            except UnicodeDecodeError:
                raise PipeEncodingError("Decode Failed")

            if err:
                raise PythonScriptError(err)

            return res
        except OSError:
            raise PythonCommunicationError("OSError")

    def write(self, s):
        '''
        Write a given string to the stdin of the python script.
        
        May raise a PythonScriptError;
        This usually indicates that the program has terminated.
        '''
        try:
            self.p.stdin.write(s.encode(stdin_encoding()))
            self.p.stdin.flush()

        except OSError:
            raise PythonCommunicationError("OSError")

    def kill(self):
        self.p.kill()


class InvalidInteractionStateError(Exception):
    pass


class Interaction():
    '''
    A class for representing a program interaction.
    An interaction is a series of inputs and outputs from and to the program.
    
    An instance of Interaction is state-based.
    That is, once an Interaction is built, you can step through it one by one, getting the input/outputs.
    
    Example:
        Say there is a program that greets the user, gets a string from the user, and tells how long the input was.
        A representation of the above program in an Interaction object might look like this:
        
        [0] OUTPUT : "Hello user! Enter string: "
        [1] INPUT  : "asdf\\n"
        [2] OUTPUT : "The string is 4 characters long.\\n"
        
        You can build the above object like so:
        inter=Interaction()
        inter.add_in("Hello user! Enter string: ")
        inter.add_out("asdf\\n")
        inter.add_in("The string is 4 characters long.\\n")
        
        And traverse through it like so:
        inter.rewind()
        inter.next() # You have to call next() to get the first result.
        inter.get_state() >> returns "OUT"
        inter.get_string() >> returns "Hello user! Enter string: "
        inter.next()
        
        and so on.
    
    interaction_type can be set as CONSOLE or INTERACTIVE.
    addicionally, words EXTENDED or COMMAND can be added. e.g. interaction_type="INTERACTIVE EXTENDED COMMAND"
    
    default interaction type is CONSOLE. It will run a PythonScript, running a python script in a seperate process,
    communication via stdin/stdout.
    another interaction type is INTERACTIVE. It will run a InteractivePythonScript, running a python script 
    and then entering a interactive console for testing.
    
    adding EXTENDED only has an effect if the primary interaction type is INTERACTIVE. It will add several convenience
    functions into the global namespace, such as a function to create a virtual text file.
    
    adding COMMAND will execute commands passed into the constructor.
    
    keyword arguments command and end_command must be a function, taking two arguments. The first argument is a string
    of the path of the current python file being tested. The second argument is the directory of the python file.
    The arguments can be None, where it won't be executed.
    
    command will be executed before the main interaction starts.
    end_command will be executed after a successful interaction. Wrong answers or errors will leave the end_command
    unexecuted.
    
    '''

    def __init__(self, interaction_type="CONSOLE", command=None, end_command=None, wait_seconds=1, name=''):
        self.data = list()
        self.position = -1
        self.interaction_type = interaction_type
        self.command = command
        self.end_command = end_command
        self.wait_seconds = wait_seconds
        self.name = name

    def add_in(self, s):
        '''
        Add a given input to the interaction.
        '''
        self.data.append(["IN", str(s) + "\n"])

    def add_in_raw(self, s):
        '''
        Add a given input to the interaction. A string conversion is not done, and a newline is not added.
        '''
        self.data.append(["IN", s])

    def add_out(self, s):
        '''
        Add a given output to the interaction.
        '''
        self.data.append(["OUT", s])

    def add_text(self, f, s):
        self.data.append(["TEXT", s, f])

    def get_position(self):
        '''
        Get the current position of the interaction.
        Zero-indexed.
        '''
        return self.position

    def get_percentage(self):
        return (self.position + 1) / len(self.data) * 100

    def rewind(self):
        '''
        Reset the interaction to the -1th position.
        '''
        self.position = -1

    def next(self):
        '''
        Go to next state.
        '''
        self.position += 1
        return self.data[self.position]

    def get_state(self):
        '''
        Get the state of the current step; "IN", "OUT" or "NOT STARTED"
        '''
        if self.position == -1:
            return "NOT STARTED"
        return self.data[self.position][0]

    def get_string(self):
        '''
        Get the string of the current step.
        '''
        if self.position == -1:
            raise InvalidInteractionStateError
        return self.data[self.position][1]

    def get_filename(self):
        if self.get_state() != "TEXT":
            raise InvalidInternalStateError
        return self.data[self.position][2]

    def over(self):
        '''
        Check if the interaction is over;
        That is, check if calling next() once more will be invalid.
        '''
        return self.position + 1 >= len(self.data)

    def get_type(self):
        return self.interaction_type


class DummyInteraction(Interaction):
    '''
    Subclass of Interaction;
    Represents an interaction WHERE THE OUTPUTS ARE UNDEFINED.
    That is, outputs are all None.
    Used for generating databases.
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

        self._make_template(*args)

    def set(self, s):
        '''
        Set the current step's data.
        '''
        self.data[self.position][1] = s

    def _make_template(self, *args):
        for i in args:
            self.add_out(None)
            self.add_in(i)
        self.add_out(None)


class ExplicitDummyInteraction(DummyInteraction):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _make_template(self, *args):
        self.add_out(None)
        for i in args:
            if i[0] == "I":
                self.add_in(i[1])
                self.add_out(None)
            elif i[0] == "T":
                self.add_text(i[1], None)
            else:
                raise InvalidInternalStateError(str(i))


## Some global variables.
py_file = None
python = None


def get_py_directory():
    global py_file
    return os.path.dirname(py_file)


def get_goal_interaction():
    '''
    Get the Interaction object corresponding to the selected Question and Test Case.
    '''
    return database[root_case_question_VAR.get()][root_case_selection.current()]


def start_button_pressed():
    global keep_looping
    keep_looping = True
    validation_start()


def validation_start():
    '''
    Start validating code.
    '''

    global had_error, keep_looping, python, root_codes_lpanel, root_codes_rpanel, goal_interaction, root, database, root_file_question_VAR, root_case_selection_VAR, loop_cleaned, infinite_read_buffer, last_read
    global inf_read_initialized

    ## Just abort if the user pressed stop/
    if not keep_looping:
        update_status("STOPPED BY USER")
        loop_complete_handler()
        return

    update_status("Initializing Python script...", progress=0)

    goal_interaction = get_goal_interaction()
    goal_interaction.rewind()

    root_codes_lpanel.clear()
    root_codes_rpanel.clear()

    ## Try to start a Python process; Display error if failed.
    try:
        if "CONSOLE" in goal_interaction.get_type():
            python = PythonScript(py_file)
        elif "INTERACTIVE" in goal_interaction.get_type():
            try:
                python = InteractivePythonScript(py_file,
                                                 extended=("EXTENDED" in goal_interaction.get_type()),
                                                 noexec=("NOEXEC" in goal_interaction.get_type()))
                os.chdir(get_py_directory())
            except UnicodeDecodeError:
                root_codes_lpanel.new_err("** Encoding Error **\nTry changing the \"File Encoding\".\n")
                update_status("Unable to execute", progress=0, color="red")

                return
            except:
                root_codes_lpanel.new_err(traceback.format_exc())
                update_status("Unable to execute", progress=0, color="red")
                return
        else:
            pass
        inf_read_initialized = False

        if "COMMAND" in goal_interaction.get_type() and goal_interaction.command != None:
            try:
                ret = eval(goal_interaction.command)(py_file, get_py_directory())
                root_codes_lpanel.new_system(str(ret) + "\n")
                root_codes_rpanel.new_system(str(ret) + "\n")
            except:
                root_codes_lpanel.new_err("Pre-Execute directives failed.\n" + traceback.format_exc())
                return

        if "WAIT" in goal_interaction.get_type():
            pass


    except PythonCommunicationError:
        root_codes_lpanel.new_err("Script load failed.\nDid you select a .py file?\n")
        return

    ## Set some loop variables
    keep_looping = True
    had_error = False

    ## Enter "Loop State"
    loop_cleaned = False
    root_case_start.configure(state="disabled")
    root_case_stop.configure(state="enabled")

    goal_interaction.next()

    ## tkinter's waiting function; We use this to loop.
    root.after(get_initialdelay(), tk_loop_read)


def validation_stop():
    '''
    Abort loop.
    '''
    global keep_looping
    keep_looping = False


## Global loop variables.
goal_interaction = None
keep_looping = False
had_error = False

infinite_read_buffer = ''
last_read = 0
inf_read_initialized = False


def tk_loop_read():
    '''
    A function to be called in the reading phase of the program.
    '''
    global python, had_error, goal_interaction, root, root_codes_lpanel, root_codes_rpanel, keep_looping, infinite_read_buffer, last_read
    global infinite_read_buffer, last_read, inf_read_initialized
    ## Loop break
    if not keep_looping:
        update_status("STOPPED BY USER")
        loop_complete_handler()
        return

    exit_now = True

    if goal_interaction.get_state() == "OUT":
        ## Try to read from the python script
        ## If there the script was terminated, display error.
        try:
            py_out = python.read()
            # print("\n\nPy out",repr(py_out))
        except PythonScriptError as e:
            root_codes_lpanel.new_err(str(e))
            update_status("Test completed and ERRORS FOUND.", progress=100, color="red")
            loop_complete_handler()
            return
        except PythonCommunicationError:
            root_codes_lpanel.new_err("** Program terminated **\n")
            update_status("Test completed and ERRORS FOUND.", progress=100, color="red")
            loop_complete_handler()
            return
        except PipeEncodingError:
            root_codes_lpanel.new_err("** Encoding Error **\nTry changing the \"Console Encoding\".\n")
            update_status("INTERNAL ERROR", progress=0, color="red")
            loop_complete_handler()
            return

        if "WAIT" in goal_interaction.get_type():
            # print("WAIT type, output:",repr(py_out))
            # print("Buffer:", repr(infinite_read_buffer))
            if not inf_read_initialized:
                infinite_read_buffer = ''
                last_read = time.time()
                update_status("WAITING FOR OUTPUT", indeterminate=True)
                inf_read_initialized = True

            already_written = infinite_read_buffer
            infinite_read_buffer += py_out
            current_time = time.time()
            exit_now = (current_time - last_read) > goal_interaction.wait_seconds
            if py_out:
                last_read = current_time
        else:
            ## Advance and notify
            update_status("TEST IN PROGRESS (out)", progress=goal_interaction.get_percentage())

        if ("INTERACTIVE" in goal_interaction.get_type()) and py_out:
            py_out += "\n"
    elif goal_interaction.get_state() == "TEXT":
        try:
            filename = os.path.join(get_py_directory(), goal_interaction.get_filename())
            root_codes_lpanel.new_system("Contents of [" + filename + "]\n" + "-" * 20 + "\n")
            root_codes_rpanel.new_system("Contents of [" + filename + "]\n" + "-" * 20 + "\n")

            with open(filename, "r") as f:
                py_out = f.read()

        except Exception:
            root_codes_lpanel.new_err(traceback.format_exc() + "\n")
            update_status("Test completed and ERRORS FOUND.", progress=100, color="red")
            loop_complete_handler()
            return

    else:
        raise InvalidInternalStateError("Why are you here " + goal_interaction.get_state())

    ## Get the "Goal" output.
    goal_out = goal_interaction.get_string()

    if (goal_out is not None) and ("WAIT" in goal_interaction.get_type()):
        if exit_now:
            goal_out = goal_out[len(already_written):]
        else:
            goal_out = goal_out[len(already_written):len(infinite_read_buffer)]

    if get_verbose_output():
        goal_out = verbosify_string(goal_out)
        py_out = verbosify_string(py_out)

    if goal_out == None:
        ## This is test case generating run
        if "WAIT" in goal_interaction.get_type():
            if exit_now:
                goal_interaction.set(infinite_read_buffer)
        else:
            goal_interaction.set(py_out)
        # root_codes_rpanel.text_remove(3)

        # root_codes_lpanel.text_remove(len(already_written))
        root_codes_lpanel.new_out(py_out)
        root_codes_rpanel.new_out("???")
    else:

        # root_codes_rpanel.text_remove(len(goal_out.replace("\n","")))
        # root_codes_lpanel.text_remove(len(already_written.replace("\n","")))
        ## A normal run
        root_codes_rpanel.new_out(goal_out)

        ## Match the string lengths by appending ▯s after.
        while len(py_out) < len(goal_out):
            py_out = py_out + "▯"

        if py_out != goal_out:
            ## Mismatch

            ## Get differences
            diff = []
            for idx in range(len(py_out)):
                try:
                    if py_out[idx] != goal_out[idx]:
                        diff.append(idx)
                except IndexError:
                    diff.append(idx)

            ## Display those differences
            root_codes_lpanel.new_out(py_out, highlight=diff)

            had_error = True
        else:
            ## Matched
            root_codes_lpanel.new_out(py_out)
    if exit_now:
        ## Go the the next phase after 1 second
        inf_read_initialized = False

        if goal_interaction.over():
            root.after(get_delay(), tk_loop_terminated)
            return

        goal_interaction.next()
        if goal_interaction.get_state() in ("IN",):
            root.after(get_delay(), tk_loop_write)
        elif goal_interaction.get_state() in ("OUT", "TEXT"):
            root.after(get_delay(), tk_loop_read)
        else:
            raise InvalidInternalStateError("Why " + goal_interaction.get_state())
    else:
        root.after(get_delay(), tk_loop_read)


def tk_loop_write():
    '''
    A function to be called in the writing phase of the program.
    '''
    global python, goal_interaction, root, root_codes_lpanel, root_codes_rpanel, keep_looping

    ## Loop break conditions
    if not keep_looping:
        update_status("STOPPED BY USER")
        loop_complete_handler()
        return

    ## advance state


    update_status("TEST IN PROGRESS (in)", progress=goal_interaction.get_percentage())

    ## read from the interaction what to write.
    to_write = goal_interaction.get_string()

    ## Display on UI first...
    to_write_ui = to_write
    if get_verbose_output():
        to_write_ui = verbosify_string(to_write)

    if "CONSOLE" in goal_interaction.get_type():
        ## Display
        root_codes_lpanel.new_in(to_write_ui)
        root_codes_rpanel.new_in(to_write_ui)
    elif "INTERACTIVE" in goal_interaction.get_type():
        ## Display
        root_codes_lpanel.new_exec(to_write_ui)
        root_codes_rpanel.new_exec(to_write_ui)

    ## Try to write to the python script
    ## If there the script was terminated, display error.
    try:
        python.write(to_write)
        # print("\n\nWrite:",repr(to_write))
    except PythonCommunicationError:
        root_codes_lpanel.new_err("** Program terminated **\n")
        update_status("Test completed and ERRORS FOUND.", progress=100, color="red")
        loop_complete_handler()
        return
    except:
        root_codes_lpanel.new_err(traceback.format_exc() + "\n")
        update_status("Test completed and ERRORS FOUND.", progress=100, color="red")
        loop_complete_handler()
        return

    if goal_interaction.over():
        root.after(get_delay(), tk_loop_terminated)
        return

    goal_interaction.next()
    ## Go the the read phase after 1 second
    root.after(get_delay(), tk_loop_read)


def tk_loop_terminated():
    '''
    A function to be called when the validation completes correctly.
    '''
    global root_case_selection, keep_looping, had_error

    ## Just abort if the user pressed stop/
    if not keep_looping:
        update_status("STOPPED BY USER")
        loop_complete_handler()
        return

    if "CONSOLE" in goal_interaction.get_type():
        try:
            python.write("test")
        except PythonCommunicationError:
            root_codes_lpanel.new_system("** Program terminated correctly **\n")
            root_codes_rpanel.new_system("** Program terminated correctly **\n")

        except:
            root_codes_lpanel.new_err(traceback.format_exc() + "\n")
            had_error = True
        else:
            root_codes_lpanel.new_err("** Program did not terminate **\n")
            had_error = True

    if "COMMAND" in goal_interaction.get_type() and goal_interaction.end_command != None and (not had_error):
        try:
            ret = eval(goal_interaction.end_command)(py_file, get_py_directory())
            root_codes_lpanel.new_system(str(ret) + "\n")
            root_codes_rpanel.new_system(str(ret) + "\n")
            # loop_cleaned = True
        except Exception as e:
            root_codes_lpanel.new_err("Post-Execute directives failed." + traceback.format_exc())
            # loop_cleaned = True
            loop_complete_handler()
            return

    ## Display accordingly.
    if had_error:
        update_status("Test completed and ERRORS FOUND.", progress=100, color="red")
    else:
        update_status("Test passed with no errors.", progress=100, color="blue")

    ## If auto-next is on, load the next case and restart validation.
    if root_case_auto_VAR.get() == 1 and not had_error:
        update_status("Test passed. Continuing to next case...", indeterminate=True, color="blue")

        ## Check if this is the last one. In that case, stop.
        size = len(root_case_selection["values"])
        current_idx = root_case_selection.current()
        next_idx = current_idx + 1
        if next_idx >= size:
            update_status("Test passed with no errors.", progress=100, color="blue")
            loop_complete_handler()
            return

        root_case_selection.current(next_idx)

        ## Go to validation start phase after 1 second.
        root.after(1000, validation_start)
    else:
        loop_complete_handler()


loop_cleaned = True


def loop_complete_handler():
    '''
    Called when the loop is completed or broken for any reason. Can be used for cleanup.

    '''
    global loop_cleaned, python, root_case_start, goal_interaction
    if loop_cleaned:
        return
    python.kill()

    root_case_start.configure(state="enabled")
    root_case_stop.configure(state="disabled")

    if goal_interaction.name.startswith("Set"):
        cases = database[root_case_question_VAR.get()]
        case_set_name = goal_interaction.name[:5]
        for i in range(len(cases)):
            if cases[i].name.startswith(case_set_name):
                root_case_selection.current(i)
                break


def get_file():
    '''
    callback for "Open File"
    '''
    f = filedialog.askopenfilename(title="Image Folder", initialdir="")
    if f == None or f == '':
        return
    global root_file_selected_VAR, py_file
    root_file_selected_VAR.set(f)
    py_file = os.path.realpath(f)

    try:
        basename=os.path.basename(py_file)
        file_q_num=basename.replace(".py","").split("_")[1]
        questions=root_case_question["values"]
        for i in questions:
            num=i.split()[1]
            #print(i)
            #print(num)
            #print(file_q_num)
            if num in file_q_num:
                root_case_question_VAR.set(i)
                reload_testcases()
                break
    except Exception:
        pass
    #print(f)
    #print(py_file)


def reload_testcases():
    '''
    Reload testcases and refresh UI.
    Called when a new problem is selected.
    '''
    global root_case_selection, root_case_question_VAR
    cases = database[root_case_question_VAR.get()]

    values = []
    for i in range(len(cases)):
        if cases[i].name:
            values.append("Test Case: " + cases[i].name)
        else:
            values.append("Test Case " + str(i + 1))

    root_case_selection["values"] = values
    root_case_selection.current(0)





def print_interaction(interaction):
    '''
    Prints a code that evaluates to an interaction.
    Used for embedding database into python source code.
    '''

    print("temp_interaction=Interaction(interaction_type=" + repr(interaction.get_type()) +
          ", command=" + repr(interaction.command) +
          ", end_command=" + repr(interaction.end_command) +
          ", wait_seconds=" + repr(interaction.wait_seconds) +
          ", name=" + repr(interaction.name) + ")")

    for i in interaction.data:
        if i[0] == "IN":
            print("temp_interaction.add_in_raw(", end='')
        elif i[0] == "OUT":
            print("temp_interaction.add_out(", end='')
        elif i[0] == "TEXT":
            print("temp_interaction.add_text(", repr(i[2]), ",", end='')
        else:
            raise InvalidInternalStateError("Why " + i[0])

        if i[1] is None:
            print("None)")
        elif i[1].count("\n") < 2:
            print(repr(i[1]) + ")")
        else:
            print()
            lines = i[1].split("\n")
            for idx in range(len(lines)):
                if idx == len(lines) - 1:
                    print("    " + repr(lines[idx]))
                else:
                    print("    " + repr(lines[idx] + "\n") + "+")
            print("    )")


def print_testcases(interactions):
    '''
    Prints code that evaluates to a list of interactins.
    '''
    print("temp_interactions=[]")
    for i in interactions:
        print_interaction(i)
        print("temp_interactions.append(temp_interaction)")


def print_database():
    '''
    prints code that evaluates to a dictionary of interactions.
    This is embedded into the source code.
    '''
    global database
    print("#### BEGIN AUTO-GENERATED CODE ####\n")
    print("database={}")
    for key in database:
        print_testcases(database[key])
        print("database[{}]=temp_interactions".format(repr(key)))
    print("\n##### END AUTO-GENERATED CODE #####")


def verbosify_string(s):
    '''
    Makes whitespace and newline easier to see.
    '''
    # return repr(s)[1:-1].replace(" ","␣")
    return s.replace(" ", "→").replace("\n", "↓\n")



## DATABASE GENERATING INPUTS L12
## This is a "Dummy" database used for building the actual test cases.
## This "Dummy" database is composed of DummyInteractions, which only has an input, and no outputs.
## When you run the program with this database, the program will add the program's outputs
## to the DummyInteraction object. This turns it into a fully built test case.
## Then, the database can be printed with print_database()
## Which prints out the built test case database
def file_writer(py_path, py_directory, filename, s):
    target_dir = os.path.join(py_directory, filename)

    with open(target_dir, 'w') as f:
        f.write(s)

    return "Creating file on [" + target_dir + "]"


def file_deleter(py_path, py_directory, filename):
    target_dir = os.path.join(py_directory, filename)

    os.remove(target_dir)

    return "Deleted file on [" + target_dir + "]"


L12P3T1 = '''Hello World
'''
L12P3T2 = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 
'''
L12P3T3 = '''Hello there
This is a simple text
I dont know what to write here
I cant even use punctuation marks man
help
'''

database = {
    "Problem 1": [DummyInteraction(r'test_dict={}',
                                   r'return_value=addDailyTemp(test_dict,"Monday",100)',
                                   r'sorted(test_dict.items())',
                                   interaction_type="INTERACTIVE",
                                   name="Normal use case"),
                  DummyInteraction(r'test_dict={}',
                                   r'return_value=addDailyTemp(test_dict,"Monday",100)',
                                   r'sorted(test_dict.items())',
                                   r'sorted(return_value.items())',
                                   interaction_type="INTERACTIVE",
                                   name="Return values"),
                  DummyInteraction(r'test_dict={"Sunday":50}',
                                   r'return_value=addDailyTemp(test_dict,"Monday",100)',
                                   r'sorted(test_dict.items())',
                                   r'sorted(return_value.items())',
                                   interaction_type="INTERACTIVE",
                                   name="Non-empty lists"),
                  DummyInteraction(r'test_dict={"Sunday":50,"Monday":70}',
                                   r'return_value=addDailyTemp(test_dict,"Monday",100)',
                                   r'sorted(test_dict.items())',
                                   r'sorted(return_value.items())',
                                   interaction_type="INTERACTIVE",
                                   name="Name clash"),
                  DummyInteraction(r'test_dict={"Sunday":50,"Monday":70}',
                                   r'return_value=addDailyTemp(test_dict,"Thursday",10)',
                                   r'sorted(test_dict.items())',
                                   r'sorted(return_value.items())',
                                   r'return_value=addDailyTemp(test_dict,"Wednesday",30)',
                                   r'sorted(test_dict.items())',
                                   r'sorted(return_value.items())',
                                   r'return_value=addDailyTemp(test_dict,"Monday",100)',
                                   r'sorted(test_dict.items())',
                                   r'sorted(return_value.items())',
                                   interaction_type="INTERACTIVE",
                                   name="Multiple calls"),
                  DummyInteraction(r'test_dict={"Sunday":50,-1:100}',
                                   r'hell=5',
                                   r'return_value=addDailyTemp(test_dict,hell,"Hot as hell")',
                                   r'sorted(test_dict.items(),key=str)',
                                   r'sorted(return_value.items(),key=str)',
                                   r'return_value=addDailyTemp(test_dict,(4,5),1234)',
                                   r'sorted(test_dict.items(),key=str)',
                                   r'sorted(return_value.items(),key=str)',
                                   interaction_type="INTERACTIVE",
                                   name="Non-string values")
                  ],
    "Problem 2": [DummyInteraction(r'test_dict={"Sun":75,"Mon":73,"Tue":60,"Wed":100,"Thu":78,"Fri":20,"Sat":-10}',
                                   r"result=moderateDays(test_dict)",
                                   r"result.sort()",
                                   r"result",
                                   interaction_type="INTERACTIVE",
                                   name="Normal use case"),
                  DummyInteraction(r'test_dict={"Sun":69,"Mon":70,"Tue":71,"Wed":78,"Thu":79,"Fri":80,"Sat":10}',
                                   r"result=moderateDays(test_dict)",
                                   r"result.sort()",
                                   r"result",
                                   interaction_type="INTERACTIVE",
                                   name="Inclusive range"),
                  DummyInteraction(r'test_dict={"Sun":0,"Mon":10,"Tue":20,"Wed":45,"Thu":100,"Fri":46,"Sat":10}',
                                   r"result=moderateDays(test_dict)",
                                   r"result.sort()",
                                   r"result",
                                   interaction_type="INTERACTIVE",
                                   name="Empty result")
                  ],
    "Problem 3": [DummyInteraction("CPChecker_L12P3T1.txt",
                                   command=r"lambda py_path,py_directory: file_writer(py_path, py_directory, 'CPChecker_L12P3T1.txt', L12P3T1)",
                                   interaction_type="CONSOLE COMMAND",
                                   name="Set 1 - Encryption"),
                  DummyInteraction("# Checking if all values from a-z, A-Z, 0-9, and space is included",
                      "csv_map=CPChecker.L12.paired_csv_parse(csv_file='CPChecker_L12P3T1.key')",
                      "sorted(csv_map.keys())",
                      interaction_type="INTERACTIVE EXTENDED NOEXEC",
                      name="Set 1 - Key coverage"),
                  DummyInteraction("# Decrypting with the internal program.\n# If this fails, it means your encryption algorithm is wrong.",
                      "CPChecker.L12.decrypt(keyfile='CPChecker_L12P3T1.key',encryptfile='CPChecker_L12P3T1.enc')",
                      interaction_type="INTERACTIVE EXTENDED NOEXEC",
                      name="Set 1 - Decryption(CPChecker)"),
                  ExplicitDummyInteraction(("I", "CPChecker_L12P3T1.enc"),
                                           ("T", "CPChecker_L12P3T1.txt"),
                                           interaction_type="CONSOLE COMMAND",
                                           name="Set 1 - Decryption(Your program)",
                                           end_command=r"lambda py_path,py_directory: file_deleter(py_path, py_directory, 'CPChecker_L12P3T1.enc')+'\n'+file_deleter(py_path, py_directory, 'CPChecker_L12P3T1.key')+'\n'+file_deleter(py_path, py_directory, 'CPChecker_L12P3T1.txt')"),

                  DummyInteraction("CPChecker_L12P3T1.txt",
                                   command=r"lambda py_path,py_directory: file_writer(py_path, py_directory, 'CPChecker_L12P3T1.txt', L12P3T2)",
                                   interaction_type="CONSOLE COMMAND",
                                   name="Set 2 - Encryption"),
                  DummyInteraction("# Decrypting with the internal program.\n# If this fails, it means your encryption algorithm is wrong.",
                      "CPChecker.L12.decrypt(keyfile='CPChecker_L12P3T1.key',encryptfile='CPChecker_L12P3T1.enc')",
                      interaction_type="INTERACTIVE EXTENDED NOEXEC",
                      name="Set 2 - Decryption(CPChecker)"),
                  ExplicitDummyInteraction(("I", "CPChecker_L12P3T1.enc"),
                                           ("T", "CPChecker_L12P3T1.txt"),
                                           interaction_type="CONSOLE COMMAND",
                                           name="Set 2 - Decryption(Your program)",
                                           end_command=r"lambda py_path,py_directory: file_deleter(py_path, py_directory, 'CPChecker_L12P3T1.enc')+'\n'+file_deleter(py_path, py_directory, 'CPChecker_L12P3T1.key')+'\n'+file_deleter(py_path, py_directory, 'CPChecker_L12P3T1.txt')"),

                  DummyInteraction("CPChecker_L12P3T1.txt",
                                   command=r"lambda py_path,py_directory: file_writer(py_path, py_directory, 'CPChecker_L12P3T1.txt', L12P3T3)",
                                   interaction_type="CONSOLE COMMAND",
                                   name="Set 3 - Encryption"),
                  DummyInteraction("# Decrypting with the internal program.\n# If this fails, it means your encryption algorithm is wrong.",
                      "CPChecker.L12.decrypt(keyfile='CPChecker_L12P3T1.key',encryptfile='CPChecker_L12P3T1.enc')",
                      interaction_type="INTERACTIVE EXTENDED NOEXEC",
                      name="Set 3 - Decryption(CPChecker)"),
                  ExplicitDummyInteraction(("I", "CPChecker_L12P3T1.enc"),
                                           ("T", "CPChecker_L12P3T1.txt"),
                                           interaction_type="CONSOLE COMMAND",
                                           name="Set 3 - Decryption(Your program)",
                                           end_command=r"lambda py_path,py_directory: file_deleter(py_path, py_directory, 'CPChecker_L12P3T1.enc')+'\n'+file_deleter(py_path, py_directory, 'CPChecker_L12P3T1.key')+'\n'+file_deleter(py_path, py_directory, 'CPChecker_L12P3T1.txt')")],
    "Problem 4": [DummyInteraction(r"3eefab",
                                   interaction_type="CONSOLE",
                                   name="Minty"),
                  DummyInteraction(r"ff3a8f",
                                   interaction_type="CONSOLE",
                                   name="Pink"),
                  DummyInteraction(r"2a720b",
                                   interaction_type="CONSOLE",
                                   name="Deep green"),
                  DummyInteraction(r"cc9cdf",
                                   interaction_type="CONSOLE",
                                   name="My favorite color"),
                  DummyInteraction(r"000000",
                                   interaction_type="CONSOLE",
                                   name="Black"),
                  DummyInteraction(r"ffffff",
                                   interaction_type="CONSOLE",
                                   name="White"),
                  DummyInteraction(r"3EefAB",
                                   interaction_type="CONSOLE",
                                   name="Capitalization")],
    "Problem 5": [DummyInteraction(r"f=Fraction(14,21)",
                                   r"f.getNumerator()",
                                   r"f.getDenominator()",
                                   r"str(f)",
                                   r"repr(f)",
                                   interaction_type="INTERACTIVE",
                                   name="Constructor/repr"),
                  DummyInteraction(r"f=Fraction(1,2)",
                                   r"f.getNumerator()",
                                   r"f.getDenominator()",
                                   r"f.setNumerator(3)",
                                   r"f.setDenominator(6)",
                                   r"f.getNumerator()",
                                   r"f.getDenominator()",
                                   r"f",
                                   interaction_type="INTERACTIVE",
                                   name="Getter/Setter"),
                  DummyInteraction(r"f=Fraction(1,2)",
                                   r"f.getNumerator()",
                                   r"f.getDenominator()",
                                   r"f.setNumerator(0)",
                                   "try:\n    f.setDenominator(0)\n    err='No error'\nexcept ValueError as e:\n    err=e",
                                   r"err",
                                   r"f.getNumerator()",
                                   r"f.getDenominator()",
                                   r"f",
                                   interaction_type="INTERACTIVE",
                                   name="Getter/Setter (zeroes)"),
                  DummyInteraction(r"f=Fraction(1,2)",
                                   r"f2=f.copy()",
                                   r"f.setNumerator(3)",
                                   r"f.setDenominator(6)",
                                   r"f",
                                   r"f2",
                                   interaction_type="INTERACTIVE",
                                   name="Copy"),
                  DummyInteraction(r"f=Fraction(1,2)",
                                   r"f.setNumerator(3)",
                                   r"f.setDenominator(6)",
                                   r"f2=f.copy()",
                                   r"f",
                                   r"f2",
                                   interaction_type="INTERACTIVE",
                                   name="Copy (Reduce)"),
                  DummyInteraction(r"f=Fraction(1,2)",
                                   r"f.setNumerator(3)",
                                   r"f.setDenominator(7)",
                                   r"f.reduce()",
                                   r"f",
                                   r"f.setNumerator(3)",
                                   r"f.setDenominator(6)",
                                   r"f.reduce()",
                                   r"f",
                                   r"f.setNumerator(3753*534)",
                                   r"f.setDenominator(3753*133)",
                                   r"f.reduce()",
                                   r"f",
                                   interaction_type="INTERACTIVE",
                                   name="Reduce"),
                  DummyInteraction(r"f=Fraction(1,2)",
                                   r"f.adjust(2)",
                                   r"f",
                                   r"f.setNumerator(3)",
                                   r"f.setDenominator(6)",
                                   r"f.adjust(2)",
                                   r"f",
                                   r"f.adjust(10)",
                                   r"f",
                                   interaction_type="INTERACTIVE",
                                   name="Adjust"),
                  DummyInteraction(r"f=Fraction(1,2)",
                                   r"f.setNumerator(-3)",
                                   r"f.setDenominator(6)",
                                   r"f.reduce()",
                                   r"f # Note: 1/-2 is also correct.",
                                   r"f.setNumerator(3)",
                                   r"f.setDenominator(-6)",
                                   r"f.reduce()",
                                   r"f # Note: -1/2 is also correct.",
                                   r"f.setNumerator(-3)",
                                   r"f.setDenominator(-6)",
                                   r"f.reduce()",
                                   r"f",
                                   interaction_type="INTERACTIVE",
                                   name="Negative Fractions")
                  ]
}

exec(db_str)

## From here on it's all UI Setup.
## Not too hard to understand.
root = Tk()
root.title("CP Checker")

root_title = Frame(root)
root_title.grid(column=1, row=1, padx=10, pady=5, sticky=(W, E, N, S))
root.columnconfigure(1, weight=1)

root_title_website = Label(root_title, text="웹사이트 - 사용법 / 업데이트 / 다음 랩 다운로드", font=("맑은 고딕", 8), foreground="blue",
                           cursor="hand2")
root_title_website.bind("<Button-1>",
                        lambda e: webbrowser.open_new(r"http://chanspi.ddns.net/Yonsei/CPChecker"))
root_title_website.grid(column=1, row=1, sticky=(W, E, N, S))

txt = '''컴퓨터프로그래밍 과제 가채점기 {} [Database: {}] {}
©컴퓨터과학과 양찬솔 - 무단 배포 허용

▯는 문자가 있어야 할 곳에 문자가 없음을 뜻합니다.'''.format(app_version, db_version, ["Release", "DEVELOPMENT VERSION"][dev])

faq_txt = '''프로그램의 출력이 제때 나타나지 않으면 >> Read/Write Delay 값을 올림
프로그램의 초기 출력이 제대로 나오지 않으면 >> Initial Delay 값을 올림
공백 문자들을 더 잘 보고 싶다면 >> Show Spaces 체크
인코딩 문제가 있으면 >> Force CP949 Encoding을 체크

이 외에 프로그램 자체에 오류 있으면 톡 주세요.'''

root_title_text = Label(root_title, text=txt, font=("맑은 고딕", 8), anchor=("nw"))
root_title_text.grid(column=1, row=2, sticky=(W, E, N, S))
root_title.columnconfigure(1, weight=1)

root_title_text = Label(root_title, text=faq_txt, font=("맑은 고딕", 8), anchor=("nw"))
root_title_text.grid(column=2, row=1, rowspan=2, sticky=(W, E, N, S))
root_title.columnconfigure(2, weight=1)
root_title.rowconfigure(2, weight=1)

root_file = LabelFrame(root, text="Python file")
root_file.grid(column=1, row=2, padx=10, pady=5, sticky=(W, E, N, S))

root_file_selectbutton = Button(root_file, text="Open", command=get_file)
root_file_selectbutton.grid(column=1, row=1, padx=5, pady=5, sticky=(W, E))

root_file_selected_VAR = StringVar()
root_file_selected = Label(root_file, textvariable=root_file_selected_VAR)
root_file_selected.grid(column=2, row=1, padx=5, pady=5, sticky=(W, E))
root_file.columnconfigure(2, weight=1)

root_case = LabelFrame(root, text="Case select")
root_case.grid(column=1, row=3, padx=10, pady=5, sticky=(W, E, N, S))

root_case_question_VAR = StringVar()
root_case_question = Combobox(root_case, width=15, textvariable=root_case_question_VAR)
root_case_question.bind("<<ComboboxSelected>>", lambda evt: reload_testcases())
db_keys = list(database.keys())
db_keys.sort()
root_case_question["values"] = db_keys
root_case_question.current(0)
root_case_question.grid(column=1, row=1, padx=5, pady=5, sticky=(W, E))

root_case_selection_VAR = StringVar()
root_case_selection = Combobox(root_case, width=40, textvariable=root_case_selection_VAR)
root_case_selection.grid(column=2, row=1, padx=5, pady=5, sticky=(W, E))

root_case_auto_VAR = IntVar()
root_case_auto_VAR.set(1)
root_case_auto = Checkbutton(root_case, text="Go to next automatically", variable=root_case_auto_VAR)
root_case_auto.grid(column=3, row=1, padx=5, pady=5, sticky=(W, E))

root_case_start = Button(root_case, text="Start", command=start_button_pressed)
root_case_start.grid(column=4, row=1, padx=5, pady=5, sticky=(W, E))

root_case_stop = Button(root_case, text="Stop", command=validation_stop)
root_case_stop.grid(column=5, row=1, padx=5, pady=5, sticky=(W, E))
root_case_stop.configure(state="disabled")

root_case_print = Button(root_case, text="Print Testcases", command=print_database)
if dev:
    root_case_print.grid(column=6, row=1, padx=5, pady=5, sticky=(W, E))

root_status = LabelFrame(root, text="Status")
root_status.grid(column=1, row=4, padx=10, pady=5, sticky=(W, E, N, S))


def update_status(s, progress=None, indeterminate=False, color="black"):
    '''
    Function for updating progress bar and status text.
    '''
    global root_status_label, root_status_bar_VAR, root_status_bar
    root_status_label.configure(text=s, foreground=color)

    if indeterminate:

        if root_status_bar.cget("mode") != "indeterminate":
            root_status_bar_VAR.set(0)
            root_status_bar.configure(mode="indeterminate", maximum=20)
            root_status_bar.start()
    else:
        root_status_bar.stop()
        root_status_bar.configure(mode="determinate", maximum=100)

    if progress == None:
        pass
    else:
        root_status_bar_VAR.set(progress)


root_status_bar_VAR = Variable()
root_status_bar = Progressbar(root_status, orient=HORIZONTAL, length=200,
                              mode='determinate', variable=root_status_bar_VAR)
root_status_bar.grid(column=1, row=1, padx=5, pady=5, sticky=(W, E))

root_status_label = Label(root_status, text="Standby")  # , justify=CENTER, anchor=CENTER, font=(None, 24))
root_status_label.grid(column=2, row=1, padx=5, pady=5, sticky=(W, E, N, S))
root_status.columnconfigure(2, weight=1)
root_status.rowconfigure(1, weight=1)

root_settings = LabelFrame(root, text="Settings")
root_settings.grid(column=1, row=5, padx=10, pady=5, sticky=(W, E, N, S))

root_settings_row1 = Frame(root_settings)
root_settings_row1.grid(row=1, column=1, sticky=(W, N, S))

root_settings_row2 = Frame(root_settings)
root_settings_row2.grid(row=2, column=1, sticky=(W, N, S))


def delay_callback(x):
    try:
        global root_settings_warning, root_settings_delay, root_settings_initialdelay
        if root_settings_delay.plus_get_value() < 0.45 or root_settings_initialdelay.plus_get_value() < 0.95:
            root_settings_warning.grid()
        else:
            root_settings_warning.grid_remove()
    except NameError:
        pass


root_settings_warning = Label(master=root_settings_row1, text="주의: Delay가 너무 낮으면 오류가 발생할 수 있습니다.", font=("맑은 고딕", 10),
                              anchor=("nw"), foreground="red")
root_settings_warning.grid(column=1, row=2, columnspan=4, padx=5, pady=5)


def get_delay():
    return int(root_settings_delay.plus_get_value() * 1000)


root_settings_delay = SliderPlus(master=root_settings_row1, plus_name="Read/Write delay", plus_max=5.0, plus_min=0.1,
                                 plus_divisions=1000, plus_format=1, plus_callback=delay_callback)
root_settings_delay.plus_set(0.5)
root_settings_delay.grid(column=1, row=1, padx=5, pady=5)


def get_initialdelay():
    return int(root_settings_initialdelay.plus_get_value() * 1000)


root_settings_initialdelay = SliderPlus(master=root_settings_row1, plus_name="Initialize delay", plus_max=5.0,
                                        plus_min=0.1,
                                        plus_divisions=1000, plus_format=1, plus_callback=delay_callback)
root_settings_initialdelay.plus_set(1)
root_settings_initialdelay.grid(column=2, row=1, padx=5, pady=5)


def get_verbose_output():
    return root_settings_verboseoutput_VAR.get() == 1


root_settings_verboseoutput_VAR = IntVar()
root_settings_verboseoutput_VAR.set(0)
root_settings_verboseoutput = Checkbutton(root_settings_row1, text="Show Spaces",
                                          variable=root_settings_verboseoutput_VAR)
root_settings_verboseoutput.grid(column=3, row=1, padx=5, pady=5, sticky=(W, E))

root_settings_fileencoding_LABEL = Label(root_settings_row2, text="File Encoding")
root_settings_fileencoding_LABEL.grid(column=1, row=1, padx=5, pady=5, sticky=(W, E))


def get_file_encoding():
    global root_settings_fileencoding_VAR
    return root_settings_fileencoding_VAR.get()


encodings_preset = ["utf_8", "cp949", "ascii", "euc_kr", "utf_16_le", "utf_16_be"]
stdout_default = sys.stdout.encoding.lower().replace("-", "_")
stdin_default = sys.stdin.encoding.lower().replace("-", "_")
if stdout_default not in encodings_preset:
    encodings_preset.append(stdout_default)
if stdin_default not in encodings_preset:
    encodings_preset.append(stdin_default)

root_settings_fileencoding_VAR = StringVar()
root_settings_fileencoding_VAR.set(encodings_preset[0])

root_settings_fileencoding = Combobox(root_settings_row2, textvariable=root_settings_fileencoding_VAR,
                                      values=encodings_preset)
root_settings_fileencoding.grid(column=2, row=1, padx=5, pady=5, sticky=(W, E))

root_settings_consoleencoding_LABEL = Label(root_settings_row2, text="Console Encoding")
root_settings_consoleencoding_LABEL.grid(column=3, row=1, padx=5, pady=5, sticky=(W, E))


def get_console_encoding():
    global root_settings_consoleencoding_VAR
    return root_settings_consoleencoding_VAR.get()


root_settings_consoleencoding_VAR = StringVar()
root_settings_consoleencoding_VAR.set(stdout_default)

root_settings_consoleencoding = Combobox(root_settings_row2, textvariable=root_settings_consoleencoding_VAR,
                                         values=encodings_preset)
root_settings_consoleencoding.grid(column=4, row=1, padx=5, pady=5, sticky=(W, E))

root_codes = Frame(root)
root_codes.grid(column=1, row=6, padx=5, pady=5, sticky=(W, E, N, S))
root.rowconfigure(6, weight=1)

root_codes_lpanel = CodePanel(root_codes, text="Your Code")
root_codes_lpanel.grid(column=1, row=1, padx=5, pady=5, sticky=(W, E, N, S))
root_codes.columnconfigure(1, weight=1)
root_codes.rowconfigure(1, weight=1)

root_codes_rpanel = CodePanel(root_codes, text="Answer")
root_codes_rpanel.grid(column=3, row=1, padx=5, pady=5, sticky=(W, E, N, S))
root_codes.columnconfigure(3, weight=1)

## Gotta do this for the first time.
reload_testcases()

## Start Tk.
root.mainloop()

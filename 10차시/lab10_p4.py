#Open data.txt to read line
data_file = open('data.txt','r')
data_list = []
#Make list and append line
for line in data_file:
    data_list.append(int(line[:-1]))
data_file.close()
#Make result list
result = []
#Calculate digit to given condition
result.append((data_list[0]+data_list[0]+data_list[1])/3)
for e in range(0,len(data_list)-2):
    result.append((data_list[e]+data_list[e+1]+data_list[e+2])/3)
result.append((data_list[len(data_list)-2]+data_list[len(data_list)-1]+data_list[len(data_list)-1])/3)
#print result
print(result)

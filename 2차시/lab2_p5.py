#Get P1's month, day, year of birth
P1_month = int(input('Person 1: Enter month born (1-12): '))
P1_day = int(input('Person 1: Enter day born(1-31): '))
P1_year = int(input('Person 1: Enter year born(4-digit): '))

#Get P2's month, day, year of birth
P2_month = int(input('Person 2: Enter month born (1-12): '))
P2_day = int(input('Person 2: Enter day born(1-31): '))
P2_year = int(input('Person 2: Enter year born(4-digit): '))

#Define the year in second and day in second
day_in_second = 60*60*24
year_in_second = day_in_second*365

#Calculate average seconds of year and seconds of day
avg_year_in_second = (year_in_second*4+day_in_second)//4
avg_month_in_second = avg_year_in_second//12

#Difference seconds of year between P1 and P2
if P2_year>=P1_year :
    year = (P2_year-P1_year)*avg_year_in_second
else:
    year = (P1_year-P2_year)*avg_year_in_second
    
#Calculate seconds of P1 and P2
P1_second = P1_month*avg_month_in_second+P1_day*day_in_second
P2_second = P2_month*avg_month_in_second+P2_day*day_in_second

#Difference seconds between P1 and P2
if P2_second>=P1_second :
    result = P2_second-P1_second + year
else :
    result = P1_second-P2_second + year
    
#output results
print('Age difference in seconds:',result)


#Get user USD
user_USD = int(input('Enter the taxable income in USD: '))

#Calculating Conditional Compliance

if user_USD < 750 :
    user_tax = user_USD * 0.01

elif user_USD>=750 and user_USD<2250 :
    user_tax = (user_USD - 750) * 0.02 + 7.50

elif user_USD>=2250 and user_USD<3750 :
    user_tax = (user_USD - 2250) * 0.03 + 37.50

elif user_USD>=3750 and user_USD<5250 :
    user_tax = (user_USD - 3750) * 0.04 + 82.50

elif user_USD>=5250 and user_USD<7000 :
    user_tax = (user_USD - 5250) * 0.05 + 142.50

else :
    user_tax = (user_USD - 7000) * 0.06 + 230.00
#Output result
print('Tax due:',format(user_tax,'.2f'),'USD')

#Define evalPolynomial function
def evalPolynomial(x):
    """This program calculate polynomial of user input x"""
    x = 3*x**5+2*x**4-5*x**3-x**2+7*x-6
    return x
#Get user x
x = int(input('Enter a value for x: '))
result = evalPolynomial(x)
#Output result
print('Polynomial for x=', x ,': ',result,sep='')

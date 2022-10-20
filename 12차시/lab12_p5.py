#
# import importlib
# importlib.reload(fraction) to reload this module.
#

class Fraction(object):

  def __init__(self, n, d):
    #Stores the value divided by the greatest common divisor.
    if n > d:
      a = n
      b = d
    elif n==d:
      n = 1
      d = 1
    else :
      a = d
      b = n
    r = a%b
    while r != 0:
      a = b
      b = r
      r = a%b
    n = n//b
    d = d//b
    
      
    self.numerator = n
    self.denominator = d

  def __str__(self):
    return str(self.numerator) + '/' + str(self.denominator)

  def reduce(self):
    """Reduces self to simplest terms. Also removes the signs
    if both numerator and denominator are negative.
    Whole numbers (1, 2, ...) are represented as 1/1, 2/1, 3/1 ...
    Raises exception ValueError if the denominator is 0.
    """
    #Stores the value divided by the greatest common divisor.
    n = self.numerator 
    d = self.denominator 
    if n > d:
        a = n
        b = d
    elif n==d:
        n = 1
        d = 1
    else :
        a = d
        b = n
    r = a%b
    while r != 0:
      a = b
      b = r
      r = a%b
    n = n//b
    d = d//b
    self.numerator = n
    self.denominator = d
    pass 
          
  def adjust(self, factor):
    """Multiplies numerator and denominator by factor."""
    #Multiply the value of factor.
    self.numerator = self.numerator*factor
    self.denominator = self.denominator*factor
    pass 


import time
import turtle

SIZE = 20 # size of the 2D cellular automaton
work = []
tmp  = []
gene = turtle.Turtle()
gene.shape('square')
gene.fillcolor('black')

def printSep():
  '''Print a separator'''
  for ctr in range(0, SIZE+2):
    print('-', end='')
  print('')

def printWorld(world):
  '''Print one generation.
      Must use printSep() above to print the separators. 
  ''' 
  print('printWorld not yet implemented')


# Initialize work and tmp:

# Compute:
while True:
  printWorld(work)
  time.sleep(1)

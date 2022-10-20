
from globals import FOODMAX,  STEPMAX, WIDTH, HEIGHT, X_MAX, Y_MAX, MS_TO_QUIT
from globals import FOOD as food, GHOSTS as ghosts
# Import our own constants:

from characters import pacman

import turtle

class auto_pacman(pacman):

  """ Class auto_pacman, the automatically navigating pacman.

      The auto_pacman class is a subclass of the pacman class. It inherits all
      data attributes and methods from the pacman class. It overrides the
      move() method of the pacman class to automatically navigate pacman
      across the screen.

      Attributes:
         ... please describe your attributes here
  """

  def move(self):
    """Eating food automatically while avoiding ghosts"""
    #Locate the ghosts, pacman
    gx1, gy1 = ghosts[0].getPosition()
    gx2, gy2 = ghosts[1].getPosition()
    pmx,pmy = self.getPosition()
    #Set the gap
    gap = 45
    try:
      #Decide where to place the food
      x, y = food[1].getPosition()
      #move in x direction
      if pmx > x+5:
        pacman.turnWest(self)
      elif pmx < x-5:
        pacman.turnEast(self)
      else:
        #Move in the y direction and avoid ghosts
        if gy1-gap < pmy and pmy < gy1+30 and gx1-30 < pmx and pmx < gx1+gap :
          pacman.turnSouth(self)
          
        elif gy2-gap < pmy and pmy < gy2+30 and gx2-30 < pmx and pmx < gx2+gap :
          pacman.turnSouth(self)
          
        elif pmy > y+5:
          pacman.turnSouth(self)
        elif pmy < y-5:
          pacman.turnNorth(self)
      self.ttl.forward(10)
      
    except :
      #Decide where to place the food
      x, y = food[0].getPosition()
      #move in x direction
      if pmx > x+5:
        pacman.turnWest(self)
      elif pmx < x-5:
        pacman.turnEast(self)
      else:
        #Move in the y direction and avoid ghosts
        if gy1-gap < pmy and pmy < gy1+30 and gx1-30 < pmx and pmx < gx1+gap :
          pacman.turnSouth(self)
          
        elif gy2-gap < pmy and pmy < gy2+30 and gx2-30 < pmx and pmx < gx2+gap :
          pacman.turnSouth(self)
          
        elif pmy > y+5:
          pacman.turnSouth(self)
        elif pmy < y-5:
          pacman.turnNorth(self)
      self.ttl.forward(10)
    #
    # 

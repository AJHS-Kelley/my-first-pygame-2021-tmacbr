# my first pygame, Tristan Mckay, 11/29/21 159 p.m, v0.0

import pygame, sys
from pygame.locals import * 

# start pygame 
  pygame.init() 

# setup window. 1
    # windowsurface = pygame.display.set_mode((500,400), 0, 32)  
    pygame.display.set_caption('hello, world!')

# setup colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
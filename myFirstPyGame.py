# my first pygame, Tristan Mckay, 11/29/21 159 p.m, v0.0

import pygame, sys
from pygame.font import SysFont
from pygame.locals import * 

 # start pygame 
pygame.init() 

# setup window. 1
WindowSurface = pygame.display.set_mode((500,400), 0, 32)  
pygame.display.set_caption('hello, world!')

# setup colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DEPRESSIONPURP = (193, 75, 253)
# setup font
basicfont = pygame.font.SysFont(None, 48)

# setup text.
text = basicfont.render('hello, world!', True, WHITE, BLUE)
textrect = text.get_rect()
textrect.centerx = WindowSurface.get_rect().centerx
textrect.centery = WindowSurface.get_rect().centery

# fill background color
WindowSurface.fill(WHITE)

# draw a polygon onto the screen.
pygame.draw.polygon(WindowSurface, DEPRESSIONPURP, ((146,0), (291, 106), (236,277), (0, 106)))

 # draw lines on screen
pygame.draw.line(WindowSurface, RED, (60,60), (120, 60), 4)
pygame.draw.line(WindowSurface, GREEN, (60,40), (120, 40), 3)
pygame.draw.line(WindowSurface, BLACK, (50,60), (100, 60), 2)


 # draw a circle
pygame.draw.circle(WindowSurface, WHITE,(300, 50), 20, 0)

# draw an ellispe
pygame.draw.ellipse(WindowSurface, BLUE, ( 300, 250, 40, 80), 1)

# draw the text rectangle
pygame.draw.rect(WindowSurface, BLUE, (textrect.left - 20, textrect.top - 20, textrect.width + 40, textrect.height + 40))

# create pixel array
pixArray = pygame.PixelArray(WindowSurface)
pixArray[480][380] = BLACK
del pixArray

# draw the text onto the surface.
WindowSurface.blit(text, textrect)

# update pygame display
pygame.display.update()

# run game into loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
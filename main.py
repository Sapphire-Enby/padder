#!/usr/bin/env python3
import pygame
import sys
from pygame_constants import * 
from nodepad import *
 
# Initialize pygame
pygame.init()
# Set up display
width, height = W_WID , W_HIG   
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Window with Box")
bg=pygame.image.load('Background.png')
arr = nodepad.create()   # generate 2d array of  pad objects

# print(arr)  # returns box boundaries      



# Set up GUI colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the rectangle (box)

# Main game loop
def gameLoop():
    running = True
    while running:
        # Handle exit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mosue_pos = pygame.mouse.get_pos()
                print(arr.check(mosue_pos))
        # pygame.draw.rect(screen, RED, (box_x, box_y, box_width, box_height))
        screen.blit(bg,(0,0))
        
        # FOR TESTING
        #for y in arr:
        #    for x in y:
        #        print(x[0])
        #        pygame.draw.rect(screen,RED,(x[0],x[1],B_WID,B_HIG))

        # Update the display
        pygame.display.flip()
if __name__ == "__main__":
    gameLoop()
    # Quit pygame
    pygame.quit()
    sys.exit()


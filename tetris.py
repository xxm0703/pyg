import pygame
from math import pi

pygame.init()
 
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

W = 21
H = 13
n = 24
w = n * W
h = n * H

size = [w, h]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Example code for the draw module")
 
done = False
clock = pygame.time.Clock()

while not done:
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
 
    screen.fill(WHITE)
    y = 0
    '''    
    while y < h:
        if y % (2 * H) != 0:
            x = 0
        else:
            x = W
        while x < w:
            pygame.draw.rect(screen, BLACK, [x, y, W, H])
            x += 2 * W
        y += H  
    '''
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 != 0:
                pygame.draw.rect(screen, BLACK, [i*W, j*H, W, H])
                
        
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()

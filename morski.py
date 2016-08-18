import pdb
import pygame
from math import pi

pygame.init()
 
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

size = [300, 300]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe")

class exes (object):
    def __init__(self, x, y):
        self.x = x * 100
        self.y = y * 100
    def draw(self):
        pygame.draw.line(screen, BLACK, [self.x+6,self.y+6], [self.x+94, self.y+94], 3)
        pygame.draw.line(screen, BLACK, [self.x+94,self.y+6], [self.x+6, self.y+94], 3)    
        print self.x
        print self.y
        
class circles(object):
    def __init__(self, x, y):
        self.x = x * 100
        self.y = y * 100
    def draw(self):
        pygame.draw.ellipse(screen, BLACK, [self.x+6, self.y+6, 88, 88], 3)                   

done = False
clock = pygame.time.Clock()


while not done:
    clock.tick(10)
    
    screen.fill(WHITE)
    y = 0
    while y < 300:
        x = 0    
        while x < 300:
             pygame.draw.rect(screen, BLACK, [x, y, 100, 100], 1)
             x += 100
        y += 100
    pygame.display.flip()
    b = 0
    X = "X"
    O = "O"
    E = "."
    
    def win():
        return  (d[0][0] == d[0][1] == d[0][2] != E
              or d[1][0] == d[1][1] == d[1][2] != E
              or d[2][0] == d[2][1] == d[2][2] != E
              or d[0][0] == d[1][0] == d[2][0] != E
              or d[0][1] == d[1][1] == d[2][1] != E
              or d[0][2] == d[1][2] == d[2][2] != E
              or d[1][1] == d[2][2] == d[0][0] != E
              or d[0][2] == d[2][0] == d[1][1] != E)
    
    d = [[E,E,E],
         [E,E,E],
         [E,E,E]]
         
    while b != 3:
        a = input("Enter cell: ")
        x = int(a) - 1
        y = int(round(10 * (a - int(a))) - 1)


        if d[x][y] != E:
            print "Sorry, that's not possible!"
            continue
        if b == 0:
            d[x][y] = X
            exes(x, y).draw()
            if win():
                print "'X' wins!!!"
                b = 3
            else:
                b = 1
            pygame.display.flip()
            continue
            
        if b == 1:        
            d[x][y] = O
            circles(x, y).draw() 
            if win():
                print "'O' wins!!!"
                b = 3
            else:    
                b = 0
            pygame.display.flip()
            continue
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

pygame.quit()

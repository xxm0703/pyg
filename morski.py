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
    def __init__(self, m):
        self.x = (m%1*1000)-100
        self.y = (m-m%1)*100-100
    def draw(self):
        pygame.draw.line(screen, BLACK, [self.x+6,self.y+6], [self.x+94, self.y+94], 3)
        pygame.draw.line(screen, BLACK, [self.x+94,self.y+6], [self.x+6, self.y+94], 3)    
        print self.x
        print self.y
class circles(object):
    def __init__(self, m):
        self.x = (m%1*1000)-100
        self.y = (m-m%1)*100-100
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
    l = []
    p = []
    while b != 3:
        a = input("Enter cell: ")
        if b == 0:
            l.append(a)
            if 1.3 in l and 1.2 in l and 1.1 in l:
                print "'X' WIN!"
                b = 3
            if 2.3 in l and 2.2 in l and 2.1 in l:
                print "'X' WIN!"
                b = 3
            if 3.3 in l and 3.2 in l and 3.1 in l:
                print "'X' WIN!"
                b = 3
            if 1.3 in l and 2.3 in l and 3.3 in l:
                print "'X' WIN!"
                b = 3
            if 1.2 in l and 2.2 in l and 3.2 in l:
                print "'X' WIN!"
                b = 3
            if 1.1 in l and 2.1 in l and 3.1 in l:
                print "'X' WIN!"
                b = 3
            if 1.1 in l and 2.2 in l and 3.3 in l:
                print "'X' WIN!"
                b = 3
            if 3.1 in l and 2.2 in l and 1.3 in l:
                print "'X' WIN!"
                b = 3
            
        elif b == 1:
            p.append(a)
            if 1.3 in p and 1.2 in p and 1.1 in p:
                print "'O' WIN!"
                b = 3
            if 2.3 in p and 2.2 in p and 2.1 in p:
                print "'O' WIN!"
                b = 3
            if 3.3 in p and 3.2 in p and 3.1 in p:
                print "'O' WIN!"
                b = 3
            if 1.3 in p and 2.3 in p and 3.3 in p:
                print "'O' WIN!"
                b = 3
            if 1.2 in p and 2.2 in p and 3.2 in p:
                print "'O' WIN!"
                b = 3
            if 1.1 in p and 2.1 in p and 3.1 in p:
                print "'O' WIN!"
                b = 3
            if 1.1 in p and 2.2 in p and 3.3 in p:
                print "'O' WIN!"
                b = 3
            if 3.1 in p and 2.2 in p and 1.3 in p:
                print "'O' WIN!"
                b = 3
        g = p + l
        if len(g) == 9:
            print "Game Over!"
            break
        if g.count(a) > 1 :
            print "Sorry, that's not possible!"
            if b == 1:
                p.pop()
            else:
                l.pop()
            continue
        if b == 0:
            exes(a).draw()
    
            pygame.display.flip()
            b = 1
            continue
            
        if b == 1:        
            circles(a).draw() 

            b = 0
            pygame.display.flip()
            continue
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

pygame.quit()

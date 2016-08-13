import pygame
from math import pi

pygame.init()
 
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

size = [400, 400]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe")

done = False
clock = pygame.time.Clock()


while not done:
    clock.tick(10)
    
    screen.fill(WHITE)
    y = 0
    while y < 400:
        x = 0    
        while x < 400:
             pygame.draw.rect(screen, BLACK, [x, y, 100, 100], 2)
             x += 100
        y += 100
    pygame.display.flip()
    b = 0
    l = []
    while True:
        a = input("Enter cell: ")
        if l.count(a) == 0:
            l.append(a)
        else:
            print "Sorry, that's not possible!"
            
        if b == 0:
            if a == 1.1:
                pygame.draw.line(screen, BLACK, [2,2], [98, 98], 3)
                pygame.draw.line(screen, BLACK, [98,2], [2, 98], 3)
                    
            elif a == 1.2:
                pygame.draw.line(screen, BLACK, [102,2], [198,98], 3)
                pygame.draw.line(screen, BLACK, [198,2], [102, 98], 3)
                    
            elif a == 1.3:
                pygame.draw.line(screen, BLACK, [202,2], [298, 98], 3)
                pygame.draw.line(screen, BLACK, [298,2], [202, 98], 3)
                    
            elif a == 2.1:
                pygame.draw.line(screen, BLACK, [2,102], [98, 198], 3)
                pygame.draw.line(screen, BLACK, [98,102], [2, 198], 3)
                 
            elif a == 2.2:
                pygame.draw.line(screen, BLACK, [102,102], [198, 198], 3)
                pygame.draw.line(screen, BLACK, [198,102], [102, 198], 3)
                    
            elif a == 2.3:
                pygame.draw.line(screen, BLACK, [202,102], [298, 198], 3)
                pygame.draw.line(screen, BLACK, [298,102], [202, 198], 3)
            
            elif a == 3.1:
                pygame.draw.line(screen, BLACK, [2,202], [98, 298], 3)
                pygame.draw.line(screen, BLACK, [98,202], [2, 298], 3)
            
            elif a == 3.2:
                pygame.draw.line(screen, BLACK, [102,202], [198, 298], 3)
                pygame.draw.line(screen, BLACK, [198,202], [102, 298], 3)
            
            elif a == 3.3:
                pygame.draw.line(screen, BLACK, [202,202], [298, 298], 3)
                pygame.draw.line(screen, BLACK, [298,202], [202, 298], 3)

            b = 1
        
        elif b == 1:        
            if a == 1.1:
                pygame.draw.ellipse(screen, BLACK, [0, 0, 100, 100], 3)
        
            elif a == 1.2:        
                pygame.draw.ellipse(screen, BLACK, [100, 0, 100, 100], 3)                

            elif a == 1.3:        
                pygame.draw.ellipse(screen, BLACK, [200, 0, 100, 100], 3)
                
            elif a == 2.1:        
                pygame.draw.ellipse(screen, BLACK, [0, 100, 100, 100], 3)                
                
            elif a == 2.2:        
                pygame.draw.ellipse(screen, BLACK, [100, 100, 100, 100], 3)
                       
            elif a == 2.3:        
                pygame.draw.ellipse(screen, BLACK, [200, 100, 100, 100], 3)                       
                       
            elif a == 3.1:        
                pygame.draw.ellipse(screen, BLACK, [0, 200, 100, 100], 3)                       
                       
            elif a == 3.2:        
                pygame.draw.ellipse(screen, BLACK, [100, 200, 100, 100], 3)                       
                        
            elif a == 3.3:        
                pygame.draw.ellipse(screen, BLACK, [200, 200, 100, 100], 3)                        
        
            b = 0
        pygame.display.flip()    
        



     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

pygame.quit()

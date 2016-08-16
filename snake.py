import pygame, random
pygame.init()

wide = 800
high = 600
snake_x = wide/2
snake_y = high/2
apple_x = random.randint(0, wide)
apple_y = random.randint(0, high)
print(apple_x, apple_y)

RED = [255, 0, 0]
GREEN = [0, 255, 0]
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]

screen = pygame.display.set_mode((wide, high))
pygame.display.set_caption("Fuck")
clock = pygame.time.Clock()

PLAY = True
change_x = 0
change_y = -1
right_eye_x = 0
right_eye_y = 0
left_eye_x = 0
left_eye_y = 0
lenght = 10
side = 10

while PLAY:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            PLAY = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change_x = -1
                change_y = 0

            elif event.key == pygame.K_RIGHT:
                change_x = 1
                change_y = 0
            elif event.key == pygame.K_UP:
                change_y = -1
                change_x = 0
            elif event.key == pygame.K_DOWN:
                change_y = 1
                change_x = 0

    snake_x += change_x
    snake_y += change_y
    right_eye_x = snake_x + 2
    right_eye_y = snake_y + 2
    left_eye_x = snake_x + 2
    left_eye_y = snake_y + 7

    screen.fill(WHITE)

    if -10 < apple_x - snake_x < 10 and -10 < apple_y - snake_y < 10:
        lenght += 10
        apple_x = random.randint(0, wide)
        apple_y = random.randint(0, high)


    pygame.draw.rect(screen, RED, [apple_x, apple_y, 10, 10])
    pygame.draw.rect(screen, GREEN, [snake_x, snake_y , side, lenght])
    pygame.draw.rect(screen, BLACK, [right_eye_x, right_eye_y, 2, 2])
    pygame.draw.rect(screen, BLACK, [left_eye_x, left_eye_y, 2, 2])
    pygame.draw.rect(screen, BLACK, [0, 0, 800, 600], 20)
    pygame.display.update()
    clock.tick(50)


pygame.quit()
quit()

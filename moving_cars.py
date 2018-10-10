import sys
import pygame
import random

from text import AQUA, BANANA, WHITE, GREY, text_to_screen, TEXT

pygame.init()

size = width, height = 1024, 768

text_posx, text_posy = (60, 330)

screen = pygame.display.set_mode(size)

car1 = pygame.image.load("car1.png")
car2 = pygame.image.load("car2.png")
background = pygame.image.load("background.png")


car1_y = 450
car1_x = width - 150

car2_y = 650
car2_x = width - 150

text = TEXT

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            print(event)

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        text = text[1:]



    # ballrect = ballrect.mo
    # ve(speed)
    # if ballrect.left < 0 or ballrect.right > width:
    #     speed[0] = -speed[0]
    # if ballrect.top < 0 or ballrect.bottom > height:
    #     speed[1] = -speed[1]

    screen.blit(background, (0, 0))
    screen.blit(car1, (car1_x, car1_y))
    screen.blit(car2, (car2_x, car2_y))

    pygame.draw.rect(screen, GREY, [text_posx, text_posy, width, 30], 0)

    text_to_screen(screen, text, text_posx, text_posy)
    pygame.display.flip()
    car1_x -= 1
    car2_x -= random.choice((0, 1, 1, 2))
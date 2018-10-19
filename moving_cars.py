import sys
import pygame
import random

from text import AQUA, BANANA, WHITE, GREY, text_to_screen, TEXT


class Lines:
    def __init__(self):
        with open('jokes.txt') as input_file:
            self.lines = [l.strip() for l in input_file.readlines() if l.strip()]
        random.shuffle(self.lines)
        self.line_number = -1

    @property
    def next(self):
        self.line_number += 1
        return self.lines[self.line_number]


pygame.init()

size = width, height = 1024, 768

text_posx, text_posy = (60, 330)

screen = pygame.display.set_mode(size)

car1 = pygame.image.load("car1.png")
car2 = pygame.image.load("car2.png")
background = pygame.image.load("background.png")
foreground = pygame.image.load("foreground.png")


car1_y = 570
car1_x = width - 150

car2_y = 650
car2_x = width - 150

lines = Lines()
text = lines.next

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if len(text) < 20:
                text += ' .. ' + lines.next
            if text[0] == event.unicode:
                text = text[1:]
                car2_x -= 12

    screen.blit(background, (0, 0))
    screen.blit(car1, (car1_x, car1_y))
    screen.blit(car2, (car2_x, car2_y))
    screen.blit(foreground, (0, 0))

    pygame.draw.rect(screen, GREY, [text_posx, text_posy, width, 30], 0)

    text_to_screen(screen, text, text_posx, text_posy)
    pygame.display.flip()
    car1_x -= random.choice((0, 0, 0, 1, 1, 0, 0, 2, 3, 0, 1, 0))

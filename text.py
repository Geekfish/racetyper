import pygame

pygame.init()

TEXT = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tristique eget ex eu porta. Cras ut vestibulum est. Quisque finibus id quam vitae rutrum. Mauris mollis nunc ligula. Nullam justo ante, efficitur vel tortor eu, lobortis luctus magna. Quisque scelerisque metus eget felis consequat, nec luctus orci tincidunt. Nullam mi felis, suscipit in lacinia eget, sodales id metus."

AQUA = (0,255,255)
BANANA = (227, 207, 87)
WHITE = (255, 255, 255)
GREY = (128,128,128)



def text_to_screen(screen, text, x, y, size=20):
    words = text.split()
    if text.startswith(" "):
        first_letter = " "
        first_bg = AQUA
        first_word_rest = ""
        rest = " ".join(words[0:])
    else:
        first_bg = None
        first_letter = words[0][0]
        first_word_rest = words[0][1:]
        rest = " " + " ".join(words[1:])

    font = pygame.font.SysFont('Arial', size)

    first_letter_rend = font.render(first_letter, True, AQUA, first_bg)
    screen.blit(first_letter_rend, (x, y))
    x += first_letter_rend.get_width()

    first_word_rest_rend = font.render(first_word_rest, True, BANANA)
    screen.blit(first_word_rest_rend, (x, y))
    x += first_word_rest_rend.get_width()

    rest_rend = font.render(rest, True, WHITE)
    screen.blit(rest_rend, (x, y))

from Prince import Prince
import pygame


def initialise_graphics():
    global background_colour, screen, font
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 16)
    width, height = 640, 480
    background_colour = 200, 200, 255
    screen = pygame.display.set_mode((width, height))


def draw_family():
    for prince in royal_family:
        prince.draw()


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.USEREVENT:
            make_announcements()


def setup_announcements():
    make_announcements.index = 0
    pygame.time.set_timer(pygame.USEREVENT, 1500)


def make_announcements():
    if make_announcements.index >= len(royal_family):
        return

    prince = royal_family[make_announcements.index]
    prince.announce()
    make_announcements.index += 1


def create_royal_family():
    nick = Prince("Nick")
    matthew = Prince("Matthew", son_of=nick)
    tom = Prince("Thomas", son_of=nick)

    nick.set_graphics(screen, font, location=(10, 10))
    matthew.set_graphics(screen, font, location=(130, 140))
    tom.set_graphics(screen, font, location=(270, 240))

    return [nick, matthew, tom]


initialise_graphics()
royal_family = create_royal_family()


setup_announcements()

while True:
    screen.fill(background_colour)
    draw_family()
    pygame.display.update()
    check_events()

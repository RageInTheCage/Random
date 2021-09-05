import pygame

from Python.Pygame import MarioSprite


def main():
    game_display = pygame.display.set_mode()
    game_is_playing = True
    mario_sprite = MarioSprite.MarioSprite(0, 0)
    sprite_group = pygame.sprite.Group()
    sprite_group.add(mario_sprite)

    clock = pygame.time.Clock()
    while game_is_playing:
        pygame.event.get()
        keys = pygame.key.get_pressed()
        game_is_playing = not keys[pygame.K_ESCAPE]
        sprite_group.draw(game_display)
        sprite_group.update()
        pygame.display.flip()
        clock.tick(5)


pygame.init()
main()
pygame.quit()

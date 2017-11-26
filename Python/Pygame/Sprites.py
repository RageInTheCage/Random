import pygame


class Sprites(object):
    def __init__(self, file_name, tiles_wide, tiles_high):
        self.image = pygame.image.load(file_name).convert_alpha()
        size = self.image.get_rect().size
        self.width = size[0]
        self.height = size[1]
        self.tiles_wide = tiles_wide
        self.tiles_high = tiles_high
        self.tile_width = self.width / self.tiles_wide
        self.tile_height = self.height / self.tiles_high

    def get_tile(self, x, y, width, height):
        cropped_image = pygame.Surface((self.tile_width, self.tile_height))
        cropped_image.blit(self.image, (0, 0),
                           (x * self.tile_width, y * self.tile_height, self.tile_width, self.tile_height))
        scaled_image = pygame.transform.smoothscale(cropped_image, (width, height))
        scaled_image.set_colorkey((0, 0, 0), pygame.RLEACCEL)
        return scaled_image

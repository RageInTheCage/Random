import pygame


def strip_from_sheet(sheet, size, columns, rows):
    frames = []
    for j in range(rows):
        for i in range(columns):
            location = (size[0] * i, size[1] * j)
            frames.append(sheet.subsurface(pygame.Rect(location, size)))
    return frames


class MarioSprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        sheet = pygame.image.load("Mario (transparent).png").convert()
        sheet.set_colorkey()
        dimensions = sheet.get_rect()
        width = dimensions.width / 10
        height = dimensions.height / 9
        self.frames = strip_from_sheet(sheet, (width, height), 10, 6)
        self.frame_index = 0
        self.image = self.get_frame()
        self.rect = self.image.get_rect()
        self.rect.move(x, y)

    def get_frame(self):
        frame = self.frames[self.frame_index]
        return pygame.transform.scale(frame, (100, 100))

    def update(self):
        self.frame_index += 1
        if self.frame_index >= len(self.frames):
            self.frame_index = 0

        self.image = self.get_frame()

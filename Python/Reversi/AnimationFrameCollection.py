import glob

import pygame


def load_image(name, size=None):
    image = pygame.image.load(name).convert()
    if size:
        image = pygame.transform.scale(image, size)
    return image


def sort_file_paths(file_path_spec):
    image_files = glob.glob(file_path_spec)
    image_files.sort()
    return image_files


class AnimationFrameCollection:
    def __init__(self, file_path_spec, size=None):
        self.images = []
        for image_file_path in sort_file_paths(file_path_spec):
            self.images.append(load_image(image_file_path, size))
        self.rect = self.images[0].get_rect()
        self.max_index = len(self.images) - 1

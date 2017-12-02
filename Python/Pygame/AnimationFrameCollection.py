import glob
import pygame


def load_image(name):
    image = pygame.image.load(name).convert()
    return image


def sort_file_paths(file_path_spec):
    image_files = glob.glob(file_path_spec)
    image_files.sort()
    return image_files


class AnimationFrameCollection:
    def __init__(self, file_path_spec):
        self.images = []
        for image_file_path in sort_file_paths(file_path_spec):
            self.images.append(load_image(image_file_path))
        self.rect = self.images[0].get_rect()

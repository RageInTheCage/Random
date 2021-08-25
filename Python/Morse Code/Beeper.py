import numpy
import pygame


def create_beep_sound_array(sound_sample_rate):
    peak_volume_loudness = 4096
    frequency_hz = 440

    sound_array = numpy.array(
        [peak_volume_loudness * numpy.sin(2.0 * numpy.pi * frequency_hz * x / sound_sample_rate)
         for x in range(0, sound_sample_rate)
         ]).astype(numpy.int16)

    return pygame.sndarray.make_sound(sound_array)


class Beeper:
    def __init__(self):
        sound_sample_rate = 44100
        pygame.mixer.pre_init(sound_sample_rate, -16, 1)  # 44.1kHz, 16-bit signed, mono
        pygame.init()
        self.beep_sound = create_beep_sound_array(sound_sample_rate)

    def beep(self, duration):
        duration = int(duration)
        self.beep_sound.play(-1)
        pygame.time.delay(duration)
        self.beep_sound.stop()

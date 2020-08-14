from pygame.sprite import Sprite
from pygame import Rect, time


class Key(Sprite):
    def __init__(self, position, image, key):
        super().__init__()

        # The button sprite consists of 2 states, so takes the first half
        self.origin_image = image
        self.image = image.subsurface(Rect(0, 0, 32, 32))

        self.rect = self.image.get_rect()
        self.rect = self.rect.move(position[0], position[1])
        self.key = key

    def pressed_down(self):
        print(self.key)
        self.image = self.origin_image.subsurface(Rect(32, 0, 32, 32))

        # TODO: Simulate mouse release
        # time.delay(2500)
        # self.image = self.origin_image.subsurface(Rect(0, 0, 32, 32))

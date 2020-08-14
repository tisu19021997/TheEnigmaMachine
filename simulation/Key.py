from pygame.sprite import Sprite
from pygame import Rect, time


class Key(Sprite):
    def __init__(self, position, image, key, pressed=False):
        super().__init__()

        # The button sprite consists of 2 states, so takes the first half
        self.image = image.subsurface(Rect(0, 0, 32, 32))
        self.origin_image = image
        self.pressed = pressed
        self.update_state(pressed)

        self.rect = self.image.get_rect()
        self.rect = self.rect.move(position[0], position[1])
        self.key = key

    def update_state(self, pressed):
        self.pressed = pressed

        if self.pressed:
            self.image = self.origin_image.subsurface(Rect(32, 0, 32, 32))
        else:
            self.image = self.origin_image.subsurface(Rect(0, 0, 32, 32))
        return self

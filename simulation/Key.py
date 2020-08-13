from pygame.sprite import Sprite


class Key(Sprite):
    def __init__(self, position, image, key):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(position[0], position[1])
        self.key = key

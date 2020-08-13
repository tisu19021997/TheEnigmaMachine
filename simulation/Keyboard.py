from os import listdir, path
from pygame.sprite import Group, OrderedUpdates
from pygame import image, math
from .Key import Key
from constants.game import PADDING, SCREEN


class Keyboard(Group):
    def __init__(self, key_path):
        super().__init__()

        key_files = sorted(listdir(key_path))
        start_pos = math.Vector2(PADDING, PADDING)

        for file_name in key_files:
            if '.png' not in file_name:
                continue

            key = file_name.split('-')[0]

            key_surface = image.load(path.join(key_path, file_name))
            key_width = key_surface.get_width()

            key_sprite = Key(image=key_surface, position=start_pos, key=key)
            self.add(key_sprite)

            new_x = start_pos.x + key_width
            new_y = start_pos.y

            if new_x >= SCREEN[0] - PADDING:
                new_y += key_surface.get_height()
                new_x = PADDING

            start_pos.update(new_x, new_y)

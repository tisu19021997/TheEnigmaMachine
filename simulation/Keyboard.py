from os import listdir, path
from pygame.sprite import Group
from pygame import image, math, mouse, sprite, Rect
from .Key import Key
from constants.game import PADDING


class Keyboard(Group):
    def __init__(self, key_path):
        super().__init__()
        self.rows = Group()

        key_folders = sorted(listdir(key_path))
        start_pos = math.Vector2(PADDING, PADDING)

        for key_folder in key_folders:
            key_names = sorted(listdir(path.join(key_path, key_folder)))
            for key_name in key_names:
                if '.png' not in key_name:
                    continue

                # File name is like 1-Q.png, so split twice.
                key = key_name.split('-')[1].split('.')[0]

                # Load key surface and add them to group
                key_surface = image.load(path.join(key_path, key_folder, key_name))
                key_width = key_surface.get_width()
                key_sprite = Key(image=key_surface, position=start_pos, key=key)
                self.add(key_sprite)

                # Padding between two keys in a row
                new_x = start_pos.x + key_width
                start_pos.update(new_x, start_pos.y)

            # Padding between two rows
            new_y = start_pos.y + PADDING
            start_pos.update(PADDING, new_y)

    def pressed_down(self):
        mouse_pos = mouse.get_pos()
        for key in self.sprites():
            if key.rect.collidepoint(mouse_pos):
                key.pressed_down()
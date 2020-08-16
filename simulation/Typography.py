import os
from pygame.font import Font
from constants.game import BLACK


class Typography:
    def __init__(self, font_path, font_size):
        font_file = os.path.join(
            os.path.abspath(os.getcwd()),
            font_path)
        self.font = Font(font_file, font_size)

    def render(self, text, is_bold=True, color=BLACK):
        return self.font.render(text, is_bold, color)

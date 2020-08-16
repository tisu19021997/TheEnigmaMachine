from pygame import draw, Rect
from constants.game import BLACK, WHITE, FONT_PATH
from simulation.Typography import Typography


class Indicator:
    def __init__(self, char, width=32, height=64):
        self.char = char
        self.width = width
        self.height = height

    def draw(self, screen, x, y):
        rect = Rect(x, y, self.width, self.height)
        draw.ellipse(screen, BLACK, rect)
        font = Typography(FONT_PATH, 32)
        text = font.render(self.char, True, WHITE)

        screen.blit(text, rect.move(self.width/4, self.height/4))

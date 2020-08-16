import pygame
from constants.game import BLACK, WHITE, FONT_PATH
from simulation.Typography import Typography


class Output:
    def __init__(self):
        self.text = ''

    def add(self, character):
        self.text += character

    def draw(self, screen):
        screen_rect = screen.get_rect().center
        font = Typography(FONT_PATH, 32)
        text = font.render(self.text, True, WHITE)

        text_rect = text.get_rect(center=(screen_rect[0], screen_rect[1] + 25))
        pygame.draw.rect(screen, BLACK, (screen_rect[0] - 160, screen_rect[1], 320, 50))
        screen.blit(text, text_rect)

    def show(self, screen):
        screen_center = screen.get_rect().center
        pygame.draw.rect(screen, BLACK, (screen_center[0] - 50, screen_center[1], 100, 50))

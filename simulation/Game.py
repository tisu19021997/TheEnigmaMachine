import pygame
import sys
from pygame.sprite import Group
from simulation.Keyboard import Keyboard
from constants.game import SCREEN, BLACK, KEYBOARD_PATH


class Game:
    def __init__(self, size=SCREEN, background=BLACK, title='Turing&Enigma'):
        self.run = False
        self.screen = pygame.display.set_mode(size)
        self.background = background
        self.keyboard = Keyboard(key_path=KEYBOARD_PATH)

        pygame.display.set_caption(title)

    def start(self):
        pygame.init()
        self.run = True
        self.loop()

    def draw(self):
        self.screen.fill(self.background)
        self.keyboard.draw(self.screen)

        pygame.display.flip()

    def handle_event(self, event):
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            self.run = False
            pygame.quit()
            sys.exit()

    def loop(self):
        while self.run:
            for event in pygame.event.get():
                self.handle_event(event)
            self.draw()

        pygame.quit()
        pygame.display.quit()

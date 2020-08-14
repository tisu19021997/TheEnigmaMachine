import pygame
import sys
from simulation.Keyboard import Keyboard
from simulation.Output import Output
from constants.game import SCREEN, BLACK, KEYBOARD_PATH


class Game:
    def __init__(self, size=SCREEN, background=BLACK, title='Turing&Enigma'):
        self.run = False
        self.screen = pygame.display.set_mode(size)
        self.background = background
        self.keyboard = Keyboard(key_path=KEYBOARD_PATH)
        self.output = Output()

        pygame.display.set_caption(title)

    def start(self):
        pygame.init()
        self.run = True
        self.loop()

    def draw(self):
        self.screen.fill(self.background)
        self.keyboard.draw(self.screen)
        self.output.render(self.screen)
        pygame.display.flip()

    def handle_event(self, event):
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            self.run = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            key = self.keyboard.pressed_down()
            if key:
                # TODO: Get output from machine
                self.output.add(key)
        elif event.type == pygame.MOUSEBUTTONUP:
            self.keyboard.pressed_up()

    def loop(self):
        while self.run:
            for event in pygame.event.get():
                self.handle_event(event)
            self.draw()

        pygame.quit()
        pygame.display.quit()

import pygame
import sys
from simulation.Keyboard import Keyboard
from simulation.Output import Output
from simulation.Indicator import Indicator
from constants.game import SCREEN, BLACK, KEYBOARD_PATH, PADDING, CENTER
from constants.alphabet import alphabet
from helper.string import in_alphabet


class Game:
    def __init__(self, machine, size=SCREEN, background=BLACK, title='Turing&Enigma'):
        self.machine = machine
        self.indicators = []
        self.update_indicator()

        self.background = background
        self.keyboard = Keyboard(key_path=KEYBOARD_PATH)
        self.output = Output()
        self.running = False
        self.screen = pygame.display.set_mode(size)

        pygame.display.set_caption(title)

    def start(self):
        pygame.init()
        self.running = True
        self.loop()

    def exit(self):
        self.running = False
        pygame.quit()
        pygame.display.quit()
        sys.exit()

    def draw(self):
        # Draw background color
        self.screen.fill(self.background)

        # Draw machine's component
        self.keyboard.draw(self.screen)
        self.output.draw(self.screen)

        init_x = CENTER[0]
        if len(self.indicators) > 0:
            for indicator in self.indicators:
                indicator.draw(self.screen, init_x, PADDING)
                init_x -= indicator.width * 2

        pygame.display.flip()

    def handle_event(self, event):
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            self.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            key = self.keyboard.pressed_down()
            if key:
                self.output.add(self.machine.encipher(key))
                self.update_indicator()
        elif event.type == pygame.MOUSEBUTTONUP:
            self.keyboard.pressed_up()
        elif event.type == pygame.KEYDOWN:
            if in_alphabet(event.key, is_ascii=True):
                # Convert ascii code to actual character
                key = pygame.key.name(event.key)
                self.output.add(self.machine.encipher(key))
                self.update_indicator()
            # TODO: Implement character deletion?
            # elif event.key == pygame.K_BACKSPACE:

    def loop(self):
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            self.draw()

        self.exit()

    def update_indicator(self):
        assert self.machine.rightmost_rotor

        rotor = self.machine.rightmost_rotor

        if not self.indicators:
            while rotor:
                indicator = Indicator(alphabet[rotor.offset % len(alphabet)])
                self.indicators.append(indicator)
                rotor = rotor.next
            return

        index = 0
        while rotor:
            self.indicators[index].char = alphabet[rotor.offset % len(alphabet)]
            index += 1
            rotor = rotor.next

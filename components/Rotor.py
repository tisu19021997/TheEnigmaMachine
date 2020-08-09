from components.Scrambler import Scrambler
from constants.alphabet import alphabet
from constants.rotor_models import models


class Rotor(Scrambler):
    # TODO: Ringstellung
    def __init__(self, model, name, offset=0):
        assert model in models.keys(), f'Rotor model given "{model}" is not correct.'
        flow, notches = models[model].values()

        super().__init__(flow, name)
        self.offset = offset
        self.notches = notches
        self.next = None
        self.prev = None

    def step(self, verbose=1):
        self.offset = (self.offset + 1) % len(alphabet)

        if verbose:
            print(f'[{self.name}] steps, now at: ', alphabet[self.offset % len(alphabet)])

        # If any neighbour rotors meet their turn-over point, they also step.
        if self.next:
            if alphabet[self.offset] in self.notches:
                self.next.step()

        return self

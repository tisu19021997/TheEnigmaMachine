from constants.alphabet import alphabet


def alpha_shift(char, num_shifts):
    return (alphabet.index(char) + num_shifts) % len(alphabet)


class Scrambler:
    def __init__(self, flow, name, offset=0):
        self.flow = flow
        self.name = name
        self.offset = offset

    def forward(self, char, verbose=1):
        encrypted = self.flow[(alphabet.index(char) + self.offset) % len(alphabet)]

        if verbose:
            print(f'[{self.name}] Fw: {char} => {alphabet[alpha_shift(encrypted, -self.offset)]}')

        return alphabet[alpha_shift(encrypted, -self.offset)]

    def backward(self, char, verbose=1):
        shifted = alphabet[alpha_shift(char, self.offset)]
        encrypted = alphabet[self.flow.index(shifted) - self.offset]

        if verbose:
            print(f'[{self.name}] Bw: {char} => {encrypted}')

        return encrypted

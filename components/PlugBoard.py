from constants.alphabet import alphabet


class PlugBoard:
    def __init__(self, pairs):
        self.pairs = []
        self.set(pairs)

    def __validate_char(self, char):
        assert char not in self.pairs, f'Plugboard got duplicate character "{char}".'
        assert char in alphabet, f'Only characters from the alphabet are allowed in plugboard, got {char}.'

    def __validate_connection_pair(self, pair):
        assert len(pair) <= 2, f'Expected each pair to have 2 characters, got {len(pair)}.'

    def __add(self, pair):
        self.__validate_connection_pair(pair)
        print(pair)
        for char in pair:
            self.__validate_char(char)
            self.pairs.append(char)

    def __set(self, pairs):
        # If pairs has already been set, empty it
        if len(self.pairs) > 0:
            self.pairs = []

        for pair in pairs:
            self.__add(pair)

    def add(self, pair):
        self.__add(pair)
        return self

    def set(self, pair):
        self.__set(pair)
        return self

    def swap(self, char, verbose=1):
        if char not in self.pairs:
            return char

        char_idx = self.pairs.index(char)

        # If the char index is even, returns the next char.
        if char_idx % 2 == 0:
            if verbose:
                print(f'[Plugboard] swaps: {char} => {self.pairs[char_idx + 1]}')
            return self.pairs[char_idx + 1]

        # Else, returns the previous char.
        if verbose:
            print(f'[Plugboard] swaps: {char} => {self.pairs[char_idx - 1]}')
        return self.pairs[char_idx - 1]

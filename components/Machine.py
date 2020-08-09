class Machine:
    def __init__(self):
        self.rotors = None
        # Rightmost rotor is the first rotor and the opposite for the leftmost one.
        # TODO: consider deleting the rightmost pointer
        self.rightmost_rotor = None
        self.leftmost_rotor = None
        self.plugboard = None
        self.reflector = None

    def _add_rotor(self, new_rotor):
        if not self.rotors:
            self.rotors = new_rotor
            # Set both head and tail to new rotor if the linked-list is empty.
            self.rightmost_rotor = new_rotor
            self.leftmost_rotor = new_rotor
            return self

        # Append new one and create link between the tail and the new rotor.
        self.leftmost_rotor.next = new_rotor
        new_rotor.prev = self.leftmost_rotor
        self.leftmost_rotor = new_rotor

        return self

    def add_rotor(self, rotor):
        return self._add_rotor(rotor)

    def add_plugboard(self, plugboard):
        self.plugboard = plugboard
        return self

    def add_reflector(self, reflector):
        self.reflector = reflector
        return self

    def feed_forward(self, char, verbose=1):
        output = char
        rotor = self.rotors

        while rotor:
            output = rotor.forward(output, verbose)
            rotor = rotor.next

        return output

    def feed_backward(self, char, verbose=1):
        output = char
        rotor = self.leftmost_rotor

        while rotor:
            output = rotor.backward(output, verbose)
            rotor = rotor.prev

        return output

    def encipher(self, message, verbose=0):
        assert self.rotors is not None, 'No rotors found.'
        encoded_message = ''

        for char in message:
            # If a plugboard is set up, swap the character.
            if self.plugboard:
                char = self.plugboard.swap(char)

            # The rightmost rotor takes a single step.
            self.rotors.step(verbose)

            # Forward flow.
            right_to_left = self.feed_forward(char, verbose)

            # If reflector is in use.
            if self.reflector:
                right_to_left = self.reflector.forward(right_to_left, verbose)

            # Backward flow.
            left_to_right = self.feed_backward(right_to_left, verbose)

            # Swap again before outputting the result.
            if self.plugboard:
                left_to_right = self.plugboard.swap(left_to_right)

            encoded_message += left_to_right

        return encoded_message

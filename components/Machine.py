class Machine:
    def __init__(self):
        # The rightmost rotor is the first rotor and the leftmost is the last one.
        self.rightmost_rotor = None
        self.leftmost_rotor = None
        self.plugboard = None
        self.reflector = None

    def __append_rotor(self, new_rotor):
        if not self.rightmost_rotor:
            # Set both head and tail to new rotor if the linked-list is empty.
            self.rightmost_rotor = new_rotor
            self.leftmost_rotor = new_rotor
            return

        # Append new one and create link between the tail and the new rotor.
        self.leftmost_rotor.next = new_rotor
        new_rotor.prev = self.leftmost_rotor
        self.leftmost_rotor = new_rotor
        return

    def add_rotor(self, rotor):
        self.__append_rotor(rotor)
        return self

    def add_plugboard(self, plugboard):
        self.plugboard = plugboard
        return self

    def add_reflector(self, reflector):
        self.reflector = reflector
        return self

    def feed_forward(self, char, verbose=1):
        output = char
        rotor = self.rightmost_rotor

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
        assert self.rightmost_rotor is not None, 'No rotors found.'
        encoded_message = ''

        for char in message:
            # If a plugboard is set up, swap the character.
            if self.plugboard:
                char = self.plugboard.swap(char, verbose)

            # The rightmost rotor takes a single step.
            self.rightmost_rotor.step(verbose)

            # Forward flow.
            right_to_left = self.feed_forward(char, verbose)

            # If reflector is in use.
            if self.reflector:
                right_to_left = self.reflector.forward(right_to_left, verbose)

            # Backward flow.
            left_to_right = self.feed_backward(right_to_left, verbose)

            # Swap again before outputting the result.
            if self.plugboard:
                left_to_right = self.plugboard.swap(left_to_right, verbose)

            encoded_message += left_to_right

        return encoded_message

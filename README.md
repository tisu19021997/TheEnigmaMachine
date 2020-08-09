# The Enigma Machine
# Workflow
  - Basic configuration: `Reflector` - `Rotor 3` - `Rotor 2` - `Rotor 1` - `Plugboard`, the character that need to be enciphered flows from right to left.
  - Two main process:
    1. **Foward**: rightmost to leftmost,
    2. **Backward**: leftmost to rightmost. 
  - When a character enters the machine, The `Plugboard` `swap()` the character to another one based on its setting.
  - The character then enters the machine and the forwarding process starts (*from right to left*).
  - There are 3 rules for each time a character enters the machine:
    1. The rightmost rotor always **takes a single step** before enciphering the character.
    2. If any rotor (except the leftmost) is positioned at its turn-over (each rotor model has different turn-over positions), then that rotor and the rotor to its left steps.
    3. No rotor steps more than once per character enciphered.
  - There are 3 rotors and they all follow the same procedure, **one's output is the next's input**.
  - The output from the last rotor goes in the `Reflector` (default to **Reflector B**) for swapping. Then the backward process starts (*from left to right*).
  - In the end, the `Plugboard` swaps the character again and output the final character.
  
# Components

## `Scrambler`
Basically, a `Scrambler` is capable of encoding a character and forwarding it (right to left) as well as decoding and "backwarding" it (left to right).  
### 1. Attributes
- `flow`: each scrambler has different "dictionary" which it uses to translate one character to another.
- `offset`: some scrambler like `Rotor` is able to step, so the translation will be changed. Taking the offset into account ensures the correctness of the translation.
- `name`: helpful for printing. 
### 2. Methods
  - `foward(char, verbose=1)`: Forward encoding a character using the `flow`. Returns the encoded character.
  - `backward(char, verbose=1)` Backward encoding a character using the `flow`. Return the encoded character.


## `Rotor`
##### instance of `Scrambler`
Each `Rotor` is a node of a linked-list of rotors in the machine. For further information about the rotor, refer [here][Rotor].
### 1. Attributes
  - `model`: Each rotor's model will come with different `notches` and `flow`. See the full list of rotor types [here][Rotor types].
    * `notches`: When a rotor past a `notch`, not only that router shift, but also its neighbour rotor. 
    * `flow`: see `Scrambler.flow`.
  - `next`: The next `Rotor` in the machine.
  - `prev`: The previous `Rotor` in the machine.

### 2. Methods
  - `step()`: increase the `offset` by `1`. Trigger the `next.step()` when the rotor is positioned at its notch (known as [turn-over][Rotor types]).

[Rotor types]: https://en.wikipedia.org/wiki/Enigma_rotor_details#Turnover_notch_positions
[Rotor]: http://users.telenet.be/d.rijmenants/en/enigmatech.htm#rotors

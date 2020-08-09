import argparse

from components.Rotor import Rotor
from components.PlugBoard import PlugBoard
from components.Machine import Machine
from components.Scrambler import Scrambler
from constants.rotor_models import models

if __name__ == '__main__':
    # Construct the Enigma Machine with 3 rotors, 1 type B reflector and a plugboard.
    rotor_1 = Rotor('rotor_i', 'Rotor I')
    rotor_2 = Rotor('rotor_ii', 'Rotor II')
    rotor_3 = Rotor('rotor_iii', 'Rotor III')
    reflector_b = Scrambler(models['reflector_b'], name='Reflector B')
    plugboard = PlugBoard(['AB', 'CD', 'EF', 'GH', 'IJ', 'KL', 'MN', 'OP', 'QR', 'ST', 'UV', 'WX', 'YZ'])
    print(plugboard.pairs)
    machine = Machine()
    machine.add_rotor(rotor_1).add_rotor(rotor_2).add_rotor(rotor_3)
    machine.add_reflector(reflector_b).add_plugboard(plugboard)

    parser = argparse.ArgumentParser()
    parser.add_argument('enci', help='encipher the message using The Enigma Machine')
    parser.add_argument('-v', '--verbose', help='whether to print the enciphering flow of the machine',
                        action='store_false')
    args = parser.parse_args()
    message = args.enci.replace(' ', '').upper()
    verbose = args.verbose
    print(verbose)
    enciphered = machine.encipher(message, verbose)

    # assert enciphered == 'wts'.replace(' ', '').upper()
    print(f'Enciphered "{message}" into: "{enciphered}"')

from constants.alphabet import alphabet


def sanitize_message(message):
    return message.replace(' ', '').upper()


def in_alphabet(char, is_ascii=False):
    if is_ascii:
        return 65 <= char <= 122
    return char in alphabet

class MorseTranslator:
    def __init__(self):
        self.morse_dictionary = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                                 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
                                 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
                                 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
                                 'X': '-..-', 'Y': '-.--', 'Z': '--..',
                                 '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                                 '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
                                 ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
                                 '(': '-.--.', ')': '-.--.-', '!': '-.-.--'}

    def encode(self, message):
        morse_code = ''

        for letter in message.upper():
            if letter in self.morse_dictionary:
                morse_code += self.morse_dictionary[letter]
            morse_code += ' '

        return morse_code

    def decode(self, morse_code):
        decrypting_dict = {v: k for k, v in self.morse_dictionary.items()}
        decipher = ''

        for glyph in morse_code.split(' '):
            if glyph in decrypting_dict:
                decipher += decrypting_dict[glyph]
            else:
                decipher += ' '

        return decipher

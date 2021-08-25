from MorseSound import MorseSound
from MorseTranslator import MorseTranslator


def get_message_to_translate(default="Hello!"):
    message = input(f"Morse to translate <{default}>: ")
    if message == '':
        return default
    return message


def main():
    morse_translator = MorseTranslator()

    message = get_message_to_translate()
    morse_code = morse_translator.encode(message)

    morse_sound = MorseSound(speed=1)
    morse_sound.echo(morse_code)

    original_message = morse_translator.decode(morse_code)
    print(original_message)


if __name__ == '__main__':
    main()
